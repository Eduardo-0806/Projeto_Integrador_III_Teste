# PROJETO INTEGRADOR III - FERRAMENTA DE AUXILIO PARA INVESTIDORES INICIANTES
O projeto desenvolvido visa realizar uma analise completa de dados na intenção de auxiliar pessoas iniciantes ou leigas na área de investimento, de modo que sejam capaz de realizar seus objetivos e atingir suas metas por meio do investimento.
Para construção dos gráficos utilizados para demonstrar visualmente as análises, foi utilizado a linguagem python. Os dados foram retirados do site [Kaggle](https://www.kaggle.com/).

## VISUALIZANDO A ANÁLISE
Para visualizar a página que contém todos os resultados da análise feita, tal como a explicação do mesmo:
- [Página](https://eduardo-0806.github.io/Projeto_Integrador_III/)

Para ver o vídeo explicativo da análise e seus resultados:
- [Vídeo]()

## ORGANIZAÇÃO REPOSITÓRIO

- [Analises](analises): Nesse diretório estão contidos os scripts Python responsáveis pela realização das análises e construção dos gráficos utilizados na página.
  * [analise_perfil.py](analises/analise_perfil.py): Script Python responsável por gerar analises relacionadas ao perfil de investidores;
  * [analise_startup_pais.py](analises/analise_startup_pais.py): Script Python responsável por gerar analises relacionadas às startup por países;
  * [analise_startup_segmento.py](analises/analise_startup_segmento.py): Scripy Python responsável por gerar analises relacionadas às startup por segmento;
- [Data](data): Nesse diretórios estão contidos os dataset utilizados para realização das análises.
  * [Original_data.csv](data/Original_data.csv): Arquivo csv contendo informações sobre pessoas que investem;
  * [global_startup_success_dataset.csv](data/global_startup_success_dataset.csv): Arquivo csv contendo informações de startup de diferentes paises e segmentos referente ao seu nível de sucesso e questões estruturais;
  * [startup_growth_investment_data.csv](data/startup_growth_investment_data.csv): Arquivo csv contendo informações de startup de diferentes países e segmentos referente a geração de renda, valorização e quantidade de investidores;
- [Imagens](imagens): Nesse diretório estão contidos as imagens de gráficos utilizados na página para visualização dos resultados da análise.
  * [Analise_Perfil](imagens/Analise_Perfil): Pasta de imagens contendo os gráficos resultantes da análise de perfis de investidores;
  * [Analise_Startup_Pais](imagens/Analise_Startup_Pais): Pasta de imagens contendo os gráficos resultantes da análise de startup por país;
  * [Analise_Startup_Segmento](imagens/Analise_Startup_Segmento): Pasta de imagens contendo os gráficos resultantes da análise de startup por segmento;
  * [Analise_Startup_Segmento_Nacional](imagens/Analise_Startup_Segmento_Nacional): Pasta de imagens contendo os gráficos resultantes da análise nacinoal de startup por segmento;
- [gerar_analises.py](gerar_analises.py): Script Python responsável por gerar todas as análises do projeto.
- [index.html](index.html): Arquivo HTML utilizado para gerar a estrutura da página contendo a explicação do projeto, tal como suas análises e resultados.
- [style.css](style.css): Arquivo CSS utilizado para estilização da página.
