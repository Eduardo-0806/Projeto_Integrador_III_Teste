import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def categorizar_idade(idade):
    if 20 <= idade <= 25:
        return '20-25'
    elif 26 <= idade <= 30:
        return '25-30'
    elif 31 <= idade <= 35:
        return '30-35'
    else:
        return 'Outros'

def gerar_grafico_analise_genero(dados):

    #Preparação Dados
    genero_counts = dados['GENDER'].value_counts()
    labels = genero_counts.index
    sizes = genero_counts.values

    #Construção Gráfico 
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=[f"{l}\n({v} - {v/sum(sizes)*100:.1f}%)" for l, v in zip(labels, sizes)],
        colors=['#5dade2', '#ec407a'], startangle=90)
    ax.set_title('Distribuição de Gênero')
    plt.savefig("imagens/Analise_Perfil/Analise_Perfil_Genero.png")
    plt.show()

def gerar_grafico_distribuicao_faixa_etaria(dados):

    #Preparação Dados
    dados['AGE'] = pd.to_numeric(dados['AGE'], errors='coerce')
    dados['Faixa Etária'] = dados['AGE'].apply(categorizar_idade)

    faixas_ordenadas = ['25-30', '30-35', '20-25']
    faixa_counts = dados['Faixa Etária'].value_counts()
    faixa_counts = faixa_counts.reindex(faixas_ordenadas).fillna(0).astype(int)

    cores_faixa = ['#4dabf7', '#1e3d59', '#a3d5f7']
    labels = faixa_counts.index
    sizes = faixa_counts.values

    #Construção Gráfico
    fig, ax = plt.subplots()

    ax.pie(sizes, labels=[f"{v}\n({v/sum(sizes)*100:.0f}%)" for v in sizes],
        colors=cores_faixa, startangle=90)
    ax.legend(labels, title="Faixa Etária", loc="center left",
            bbox_to_anchor=(1, 0.5), fontsize=10)
    ax.set_title('Distribuição Faixa Etária')
    plt.savefig("imagens/Analise_Perfil/Analise_Perfil_Faixa_Etaria.png")
    plt.show()

def gerar_grafico_analise_objetivo(dados):

    #Preparação Dados
    objetivos_counts = dados['What is your investment objective?'].value_counts()
    labels = objetivos_counts.index
    sizes = objetivos_counts.values

    #Construção Gráfico
    fig, ax = plt.subplots()
    cores_faixa = ['#4dabf7', '#1e3d59', '#a3d5f7']

    ax.pie(sizes, labels=[f"{l}\n({v} - {v/sum(sizes)*100:.1f}%)" for l, v in zip(labels, sizes)],
        colors=cores_faixa, startangle=90)
    ax.set_title('Objetivo do Investimento')
    plt.savefig("imagens/Analise_Perfil/Analise_Perfil_Objetivo.png")
    plt.show()

def gerar_grafico_analise_expectativa_retorno(dados):
    
    #Preparação Dados
    retorno_counts = dados['How much return do you expect from any investment instrument?'].value_counts()

    #Construção Gráfico

    fig, ax = plt.subplots()
    sns.barplot(y=retorno_counts.index, x=retorno_counts.values,
                ax=ax, palette='Blues_r')
    ax.set_title('Expectativa de Retorno')
    ax.set_xlabel('QTD')
    ax.set_ylabel('Retorno Esperado')

    plt.savefig("imagens/Analise_Perfil/Analise_Perfil_Expectativa_Retorno.png")
    plt.show()

def gerar_grafico_analise_fonte_informacao(dados):

    #Preparação Dados
    fonte_counts = dados['Your sources of information for investments is '].value_counts()

    #Construção Gráfico
    fig, ax = plt.subplots()
    sns.barplot(x=fonte_counts.index, y=fonte_counts.values,
                ax=ax, palette='Blues')
    ax.set_title('Fontes de Informação')
    ax.set_ylabel('QTD')
    ax.set_xlabel('Fonte')
    ax.tick_params(axis='x', rotation=25)

    plt.tight_layout()
    plt.savefig("imagens/Analise_Perfil/Analise_Perfil_Fonte_Informacao.png")

    plt.show()

def gerar_analise_perfil(dados):
    gerar_grafico_analise_genero(dados)
    gerar_grafico_distribuicao_faixa_etaria(dados)
    gerar_grafico_analise_objetivo(dados)
    gerar_grafico_analise_expectativa_retorno(dados)
    gerar_grafico_analise_fonte_informacao(dados)

