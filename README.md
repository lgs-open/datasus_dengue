# Web Scraping de dados sobre a dengue disponibilizados pelo DATASUS.

Neste projeto fazemos download dos dados referente a dengue de 2014 em diante no Brasil disponibilizados pelo [DATASUS](https://datasus.saude.gov.br/acesso-a-informacao/doencas-e-agravos-de-notificacao-de-2007-em-diante-sinan/). Algumas observações importantes sobre o arquivo `web_scraping.py`:

1. O arquivo extraído possui a seguinte padrão de nomenclatura: `<ano>_<linha>_<coluna>_<estado>.csv`;
2. É possível escolher 1 das 27 unidades federativas (26 estados e o distrito federal). Essa escolha é feita através do `dic_estados`;
3. Existem 45 parâmetros para cada linha (disponível em `lista_linhas`) e 37 parâmetros para coluna (disponível em `dic_coluna`);
5. É possível fixar a coluna através do `dic_coluna` e obter 44 arquivos (excluindo a possilidade do parâmetro linha igual a coluna) varrendo toda a lista (`lista_linhas`) ou selecionar apenas o intervalo desejado dentro da lista de linhas;
5. A lista `anos` deve ser preenchido com o ano ou os anos escolhidos;
6. A configuração padrão é:
   - coluna: `ano_notif`;
   - anos: `14` e `15`;
   - linhas: `ano_1_sintomas`, `mes_1_sintomas` e `semana_epid_1_sintomas`.
7. O local de download é configurado no parâmetro `dir_raw`.

O arquivo `config.py` carrega informações sobre todas as linhas (`lista_linhas`), colunas (`dic_coluna`) e dos estados (`dic_estados`) disponíveis para extração.

Sinta-se à vontade para enviar dúvidas e sugestões.

Lucas G. dos Santos.

 
