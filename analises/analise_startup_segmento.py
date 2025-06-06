import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def gerar_grafico_soma_valor_estimado(dados, nacional):
    
    #Definindo Caminho da Imagem
    if nacional:
        caminho = "imagens/Analise_Startup_Segmento_Nacional/Analise_Startup_Segmento_Nacional_Soma_Valorizacao"
    else:
        caminho = "imagens/Analise_Startup_Segmento/Analise_Startup_Segmento_Soma_Valorizacao"
    
    #Preparação Dados
    series_valorizacao_segmento = dados.groupby("Industry")["Valuation (USD)"].sum()
    series_valorizacao_segmento = (series_valorizacao_segmento / 1000000000000).round(3)
    series_valorizacao_segmento.sort_values(ascending= False, inplace=True)

    #Criação Gráfico
    fg, ax = plt.subplots()
    sns.barplot(x=series_valorizacao_segmento.index, y=series_valorizacao_segmento.values,
                ax=ax, palette='Blues')
    plt.title("Soma de Valor Estimado por Segmento", fontsize=12, fontweight='bold', pad=10)
    plt.ylabel("Valor (USD)")
    plt.xticks(rotation=45, ha='right')

    for p in ax.patches:
        height = p.get_height()
        ax.text(
            p.get_x() + p.get_width() / 2.,
            height + 0.01,                    
            f'${height:.2f}T',                 
            ha='center', va='bottom', fontsize=10
        )

    plt.tight_layout()
    plt.savefig(caminho)
    plt.show()

def gerar_grafico_total_investimento_anual(dados, nacional):
    
    #Definindo Caminho da Imagem
    if nacional:
        caminho = "imagens/Analise_Startup_Segmento_Nacional/Analise_Startup_Segmento_Nacional_Total_Investimento"
    else:
        caminho = "imagens/Analise_Startup_Segmento/Analise_Startup_Segmento_Total_Investimento"

    #Preparação Dados
    series_total_investimento = dados.groupby("Year Founded")["Investment Amount (USD)"].sum()
    series_total_investimento = (series_total_investimento / 1000000000000).round(3)

    #Criação Gráfico
    plt.plot(series_total_investimento, color="cyan")
    plt.title("Total de Investimento em Startup Por Ano", fontsize=12, fontweight='bold', pad=10)
    plt.ylabel("Valor (USD)")
    plt.savefig(caminho)
    plt.show()

def gerar_tabela_quantidade_startup_por_segmento(dados, nacional):
    
    #Definindo Caminho da Imagem
    if nacional:
        caminho = "imagens/Analise_Startup_Segmento_Nacional/Analise_Startup_Segmento_Nacional_QTD"
    else:
        caminho = "imagens/Analise_Startup_Segmento/Analise_Startup_Segmento_QTD"

    #Preparação Dados
    quantidade = dados["Industry"].value_counts()
    porcentagem = (dados["Industry"].value_counts(normalize=True) * 100).round(2)

    df_quantidade_startup = pd.DataFrame({"Segmento": quantidade.index, "Quantidade": quantidade.values, "%": porcentagem.values})
    df_quantidade_startup.sort_values(by="Quantidade", ascending=False, inplace=True)
    df_quantidade_startup.loc[len(df_quantidade_startup)] = {"Segmento": "Total", "Quantidade": sum(quantidade.values), 
                                                            "%": sum(porcentagem.values)}

    # Criar a tabela
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off')

    cell_colors = [['#1a3a5f', '#2a4a7f', '#4065a3']] * (len(df_quantidade_startup)-1) + [['#8a6bd1', '#8a6bd1', '#8a6bd1']]
    table = ax.table(
        cellText=df_quantidade_startup.values,
        colLabels=df_quantidade_startup.columns,
        cellLoc='center',
        loc='center',
        colColours=['#3a6ea5'] * 3,
        cellColours=cell_colors
    )

    #Destacar o Cabeçalho e Total
    for (i, j), cell in table.get_celld().items():
        if i == 0 or i == len(df_quantidade_startup):
            cell.set_text_props(weight='bold', color='white')
        cell.set_edgecolor('white')

    # Estilo da tabela
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2)
    plt.title("Quantidade de Startup por Segmento", fontsize=14, fontweight='bold', color='white', pad=20)
    plt.savefig(caminho)
    plt.show()

def gerar_tabela_valor_investido_por_segmento(dados, nacional):
    
    #Definindo Caminho da Imagem
    if nacional:
        caminho = "imagens/Analise_Startup_Segmento_Nacional/Analise_Startup_Segmento_Nacional_Valor_Investido"
    else:
        caminho = "imagens/Analise_Startup_Segmento/Analise_Startup_Segmento_Valor_Investido"

    #Preparação Dados
    soma_valores = dados.groupby("Industry")["Investment Amount (USD)"].sum()
    porcentagem = (soma_valores/soma_valores.sum()* 100)

    df_investimento_por_segmento = pd.DataFrame({"Segmento": soma_valores.index, "Valor Investido Total(USD)": soma_valores.values,
                                    "%": porcentagem.values})
    df_investimento_por_segmento["%"] = df_investimento_por_segmento["%"].round(2)
    df_investimento_por_segmento["Valor Investido Total(USD)"] = (df_investimento_por_segmento["Valor Investido Total(USD)"]/1000000000000).round(2)
    df_investimento_por_segmento.sort_values(by="Valor Investido Total(USD)", ascending=False, inplace=True)
    df_investimento_por_segmento.loc[len(df_investimento_por_segmento)] = {"Segmento": "Total", 
                                                                        "Valor Investido Total(USD)": 
                                                                        sum(df_investimento_por_segmento["Valor Investido Total(USD)"]),
                                                                        "%": sum(porcentagem)}

    #Criação tabela

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off')

    cell_colors = [['#1a3a5f', '#2a4a7f', '#4065a3']] * (len(df_investimento_por_segmento)-1) + [['#8a6bd1', '#8a6bd1', '#8a6bd1']]

    table = ax.table(
        cellText=df_investimento_por_segmento.values,
        colLabels=df_investimento_por_segmento.columns,
        cellLoc='center',
        loc='center',
        colColours=['#3a6ea5'] * 3,
        cellColours = cell_colors
    )

    #Destacar o Cabeçalho e Total
    for (i, j), cell in table.get_celld().items():
        if i == 0 or i == len(df_investimento_por_segmento):
            cell.set_text_props(weight='bold', color='white')
        cell.set_edgecolor('white')

    # Estilo da tabela
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    # Título
    plt.title("Valor Investidor por Segmento", fontsize=12, fontweight='bold', pad=10)
    plt.tight_layout()
    plt.savefig(caminho)
    plt.show()

def gerar_grafico_receita_anual_por_segmento(dados, nacional):
    
    #Definindo Caminho da Imagem
    if nacional:
        caminho = "imagens/Analise_Startup_Segmento_Nacional/Analise_Startup_Segmento_Nacional_Receita_Anual"
    else:
        caminho = "imagens/Analise_Startup_Segmento/Analise_Startup_Segmento_Receita_Anual"

    #Preparação Dados
    soma_valores = dados.groupby("Industry")["Annual Revenue ($M)"].sum()
    soma_valores = soma_valores//1000
    soma_valores.sort_values(ascending= True, inplace=True)

    
    #Criação tabela
    fig, ax = plt.subplots(figsize=(6, 4))
    rects = plt.barh(soma_valores.index, soma_valores.values)

    for rect, valor in zip(rects, soma_valores.values):
       x = rect.get_width() + 0.1  # Ajusta a posição do texto para fora da barra
       y = rect.get_y() + rect.get_height() / 2  # Posição no meio da barra
       plt.text(x, y, str(valor), ha='left', va='center')
    
    # Título
    plt.title("Soma da Receita Anual por Segmento", fontsize=12, fontweight='bold', pad=10)
    plt.xlabel("Valor(Em Bilhões US$)")
    plt.tight_layout()
    plt.savefig(caminho)
    plt.show()

def gerar_grafico_estagio_desenvolvimento_segmento(dados,nacional):
    if nacional:
        caminho = "imagens/Analise_Startup_Segmento_Nacional/Analise_Startup_Segmento_Nacional_Estagio_Desenvolvimento"
    else:
        caminho = "imagens/Analise_Startup_Segmento/Analise_Startup_Segmento_Estagio_Desenvolvimento"

    pivot_table = pd.crosstab(dados['Industry'], dados['Funding Stage'])
    pivot_table = pivot_table.loc[pivot_table.sum(axis=1).sort_values(ascending=False).index]

    # Criar o gráfico de barras empilhadas
    ax = pivot_table.plot(kind='bar', stacked=True, figsize=(14, 7))

    for bar_index, industry in enumerate(pivot_table.index):
        y_offset = 0
        for stage in pivot_table.columns:
            value = pivot_table.loc[industry, stage]
            if value > 0:
                ax.text(
                    bar_index,
                    y_offset + value / 2,
                    str(value),
                    ha='center',
                    va='center',
                    fontsize=8,
                    color='white'  # Melhor contraste dentro das cores
                )
                y_offset += value

    # Personalizar o gráfico
    plt.title('Quantidade de Startups por Estágio de Investimento em Cada Setor')
    plt.xlabel('Segmento')
    plt.ylabel('Número de Startups')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Estágio de Investimento', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Mostrar o gráfico
    plt.savefig(caminho)
    plt.show()

def gerar_tabela_media_funcionarios_por_segmento(dados,nacional):
    if nacional:
        caminho = "imagens/Analise_Startup_Segmento_Nacional/Analise_Startup_Segmento_Nacional_Media_Funcionario"
    else:
        caminho = "imagens/Analise_Startup_Segmento/Analise_Startup_Segmento_Media_Funcionario"

    media_funcionarios = dados.groupby("Industry")["Number of Employees"].mean()
    porcentagem = (media_funcionarios/media_funcionarios.sum()* 100)

    df_porcentagem_media_funcionarios = pd.DataFrame({"Segmento": media_funcionarios.index, 
    "Média de Funcionários": media_funcionarios.values, "%": porcentagem.values})

    df_porcentagem_media_funcionarios["%"] = df_porcentagem_media_funcionarios["%"].round(2)
    df_porcentagem_media_funcionarios.sort_values(by="Média de Funcionários", ascending=False, inplace=True)
    df_porcentagem_media_funcionarios.loc[len(df_porcentagem_media_funcionarios)] = {"Segmento": "Total", 
                                                                        "Média de Funcionários": 
                                                                        df_porcentagem_media_funcionarios["Média de Funcionários"].mean(),
                                                                        "%": f"{sum(porcentagem):.0f}"}
    df_porcentagem_media_funcionarios["Média de Funcionários"] = df_porcentagem_media_funcionarios["Média de Funcionários"].round(2)
    #Criação tabela

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axis('off')
    cell_colors = [['#1a3a5f', '#2a4a7f', '#4065a3']] * (len(df_porcentagem_media_funcionarios)-1) + [['#8a6bd1', '#8a6bd1', '#8a6bd1']]

    table = ax.table(
        cellText=df_porcentagem_media_funcionarios.values,
        colLabels=df_porcentagem_media_funcionarios.columns,
        cellLoc='center',
        loc='center',
        colColours=['#3a6ea5'] * 3,
        cellColours = cell_colors
    )

    #Destacar o Cabeçalho e Total
    for (i, j), cell in table.get_celld().items():
        if i == 0 or i == len(df_porcentagem_media_funcionarios):
            cell.set_text_props(weight='bold', color='white')
        cell.set_edgecolor('white')

    # Estilo da tabela
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    # Título
    plt.title("Média de Funcionários de Startup por Segmento", fontsize=12, fontweight='bold', pad=10)
    plt.tight_layout()
    plt.savefig(caminho)
    plt.show()
    

def gerar_analise_startup_segmento(dados, nacional):
    if nacional:
        dados = dados[dados["Country"] == "Brazil"]
    gerar_grafico_soma_valor_estimado(dados, nacional)
    gerar_grafico_total_investimento_anual(dados, nacional)
    gerar_tabela_quantidade_startup_por_segmento(dados, nacional)
    gerar_tabela_valor_investido_por_segmento(dados, nacional)

def gerar_analise_startup_segmento_complementar(dados,nacional):
    if nacional:
        dados = dados[dados["Country"] == "Brazil"]
    gerar_grafico_receita_anual_por_segmento(dados,nacional)
    gerar_grafico_estagio_desenvolvimento_segmento(dados,nacional)
    gerar_tabela_media_funcionarios_por_segmento(dados,nacional)