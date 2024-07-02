
# Importando bibliotecas e módulos.
from bs4 import BeautifulSoup
import requests
from urllib import request
import urllib.request
import config
import os

# Definindo o diretório de download.
dir_raw = 'src\\data\\raw'
PATH_DIR_RAW = os.path.join(os.getcwd(), dir_raw)

def requisicao(pedido: str, path_link: str, estado: str, tentativas = 10) -> requests.models.Response:
    ''' Solicita a requisição e busca o HTML.'''   

    cookies = {
    'TS014879da': '01e046ca4c0a8d9bd5a4d20597e10626810d31936460176eb2186bf329f93ec76b99ce5d760799d4288fb05f4c38758f474fb50516',
                }
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,pt-BR;q=0.7,pt;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'TS014879da=01e046ca4c0a8d9bd5a4d20597e10626810d31936460176eb2186bf329f93ec76b99ce5d760799d4288fb05f4c38758f474fb50516',
    'Origin': 'http://tabnet.datasus.gov.br',
    'Referer': f'http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinannet/cnv/dengueb{estado}.def',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    response = requests.post(
    path_link,
    cookies=cookies,
    headers=headers,
    data=pedido,
    verify=False,
    )
    
    return response
    

def extracao(response: requests.models.Response, linha: list, coluna: list, estado:str, ano: int) -> tuple[BeautifulSoup, str]:
    '''Formata o HTML e cria o nome do arquivo sem tipagem.'''

    soup = BeautifulSoup(response.text, 'html.parser')
    file_name = f'ano{ano}_{linha[1]}_{coluna[1]}_{estado}'
    return soup, file_name


def download_file(path_download: str, file_name: str) -> None:  
    '''Verifica se o caminho existe e faz o download do arquivo.'''

    global PATH_DIR_RAW
    try:
        
        if not os.path.exists(PATH_DIR_RAW):
            raise FileNotFoundError(f'O diretório {PATH_DIR_RAW} não existe')
            
        else:
            path_file = os.path.join(PATH_DIR_RAW, file_name)
            if os.path.exists(path_file):
                print(f'Arquivo: "{file_name}" já existe.\n Atualizando arquivo...')
                os.remove(path_file)
                urllib.request.urlretrieve(path_download, f'{PATH_DIR_RAW}\\{file_name}')
                print('Arquivo atualizado.')
            else:
                urllib.request.urlretrieve(path_download, f'{PATH_DIR_RAW}\\{file_name}') # aqui faz o download e salva
                print(f'Arquivo "{file_name}" criado')
            
    except FileNotFoundError as e:
        print(f'Ocorreu um erro: {e}') 
        

def pedido(linha: list, coluna: list, estado:str, ano: int) -> None:
     '''Cria a variável e o caminho de solicitação, faz a requisição e cria um arquivo .csv.'''

     data = f'Linha={linha[0]}&Coluna={coluna[0]}&Incremento=Casos_Prov%E1veis&Arquivos=deng{estado}{ano}.dbf&pesqmes1=Digite+o+texto+e+ache+f%E1cil&SAno_1%BA_Sintoma%28s%29=TODAS_AS_CATEGORIAS__&pesqmes2=Digite+o+texto+e+ache+f%E1cil&SM%EAs_1%BA_Sintoma%28s%29=TODAS_AS_CATEGORIAS__&pesqmes3=Digite+o+texto+e+ache+f%E1cil&SSemana_epidem._1%BA_Sintomas%28s%29=TODAS_AS_CATEGORIAS__&pesqmes4=Digite+o+texto+e+ache+f%E1cil&SAno_notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes5=Digite+o+texto+e+ache+f%E1cil&SM%EAs_notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes6=Digite+o+texto+e+ache+f%E1cil&SSemana_epidem._notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes7=Digite+o+texto+e+ache+f%E1cil&SAno_epidem._notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes8=Digite+o+texto+e+ache+f%E1cil&SAno_epidem._1%BA_Sintomas%28s%29=TODAS_AS_CATEGORIAS__&pesqmes9=Digite+o+texto+e+ache+f%E1cil&SMunic%EDpio_de_notifica%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes10=Digite+o+texto+e+ache+f%E1cil&SRegi%E3o_de_Sa%FAde_%28CIR%29_de_notif=TODAS_AS_CATEGORIAS__&SMacrorreg.de_Sa%FAde_de_notific=TODAS_AS_CATEGORIAS__&SDiv.adm.estadual_de_notific=TODAS_AS_CATEGORIAS__&pesqmes13=Digite+o+texto+e+ache+f%E1cil&SMicrorregi%E3o_IBGE_de_notific=TODAS_AS_CATEGORIAS__&pesqmes14=Digite+o+texto+e+ache+f%E1cil&SReg.Metropolit%2FRIDE_de_notific=TODAS_AS_CATEGORIAS__&pesqmes15=Digite+o+texto+e+ache+f%E1cil&SMunic%EDpio_de_resid%EAncia=TODAS_AS_CATEGORIAS__&pesqmes16=Digite+o+texto+e+ache+f%E1cil&SRegi%E3o_de_Sa%FAde_%28CIR%29_de_resid=TODAS_AS_CATEGORIAS__&SMacrorreg.de_Sa%FAde_de_resid%EAnc=TODAS_AS_CATEGORIAS__&SDiv.adm.estadual_de_resid%EAncia=TODAS_AS_CATEGORIAS__&pesqmes19=Digite+o+texto+e+ache+f%E1cil&SMicrorregi%E3o_IBGE_de_resid%EAnc=TODAS_AS_CATEGORIAS__&pesqmes20=Digite+o+texto+e+ache+f%E1cil&SReg.Metropolit%2FRIDE_de_resid=TODAS_AS_CATEGORIAS__&SAutoctone_Mun_Res=TODAS_AS_CATEGORIAS__&pesqmes22=Digite+o+texto+e+ache+f%E1cil&SPa%EDs_F._infec%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes23=Digite+o+texto+e+ache+f%E1cil&SUF_F.infec%E7%E3o=TODAS_AS_CATEGORIAS__&pesqmes24=Digite+o+texto+e+ache+f%E1cil&SMunic%EDpio_infec%E7%E3o=TODAS_AS_CATEGORIAS__&SCaso_aut%F3ctone_munic_resid=TODAS_AS_CATEGORIAS__&pesqmes26=Digite+o+texto+e+ache+f%E1cil&SFaixa_Et%E1ria=TODAS_AS_CATEGORIAS__&SRa%E7a=TODAS_AS_CATEGORIAS__&SSexo=TODAS_AS_CATEGORIAS__&pesqmes29=Digite+o+texto+e+ache+f%E1cil&SClass._Final=TODAS_AS_CATEGORIAS__&SCriterio_conf.=TODAS_AS_CATEGORIAS__&SEvolu%E7%E3o=TODAS_AS_CATEGORIAS__&SExame_sorol%F3gico_%28IgM%29_Dengue=TODAS_AS_CATEGORIAS__&SExame_sorologia_Elisa________=TODAS_AS_CATEGORIAS__&SExame_isolamento_viral_______=TODAS_AS_CATEGORIAS__&SExame_de_RT-PCR______________=TODAS_AS_CATEGORIAS__&SSorotipo_____________________=TODAS_AS_CATEGORIAS__&SExame_de_Histopatologia______=TODAS_AS_CATEGORIAS__&SExame_de_Imunohistoqu%EDmica___=TODAS_AS_CATEGORIAS__&SOcorreu_hospitaliza%E7%E3o_______=TODAS_AS_CATEGORIAS__&formato=table&mostre=Mostra'
     path_link = f'http://tabnet.datasus.gov.br/cgi/tabcgi.exe?sinannet/cnv/dengueb{estado}.def'
     pedido = extracao(requisicao(data, path_link, estado), linha, coluna, estado, ano)
     path_download = f'http://tabnet.datasus.gov.br{pedido[0].find_all("a")[4].get("href")}'
     file_name = f'{pedido[1]}.csv'
     return  download_file(path_download, file_name)

def parametros(anos, coluna, linhas, estado):
    '''Recebe os parâmetros dos arquivos.'''
    for ano in anos:
        for linha in linhas:
            if linha[0] != coluna[0]:
                pedido(linha, coluna, estado, ano)
            else:
                pass

# Escolha da coluna.
coluna = config.dic_coluna['ano_notif']

# Escolha do(s) ano(s).
anos = [14, 15]

# Escolha da(s) linha(s).
linhas = config.lista_linhas[0:3] # todas as linhas

# Escolha do estado.
estado = config.dic_estados['parana']

# Pedido dos arquivos.
parametros(anos, coluna, linhas, estado)

