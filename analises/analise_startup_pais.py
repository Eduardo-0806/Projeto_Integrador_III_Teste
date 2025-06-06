import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_grafico_media_de_crescimento(dados):
    
    #Preparação dos Dados
    df_media_crescimento = dados.groupby('Country')['Growth Rate (%)'].mean().sort_values(ascending=False)

    # Construção do gráfico
    plt.figure(figsize=(12, 8))
    ax = sns.barplot(x=df_media_crescimento.values, y=df_media_crescimento.index, palette='Blues_r')
    plt.title('Média de Porcentagem de Crescimento por País\n(Ordenado por Desempenho)', fontsize=14, pad=20)
    plt.xlabel('Média de Crescimento (%)', fontsize=12)
    plt.ylabel('País', fontsize=12)

    # Adicionar valores nas barras
    for i, value in enumerate(df_media_crescimento.values):
        ax.text(value + 0.5, i, f'{value:.1f}%', va='center', color='white', fontweight='bold')

    plt.tight_layout()

    #Salvar e Exibir Gráfico
    plt.savefig('imagens/Analise_Startup_Pais/Analise_Startup_Pais_Crescimento.png')
    plt.show()

def gerar_grafico_quantidade_investidores_pais(dados):

    #Preparação Dados
    plt.figure(figsize=(12, 8))
    df_investidor_pais = dados.groupby('Country')['Number of Investors'].sum().sort_values(ascending=False)

    # Construção Gráfico
    ax = sns.barplot(x=df_investidor_pais.values, y=df_investidor_pais.index, palette='Blues_r')
    plt.title('Total de Investidores por País', fontsize=14, pad=20)
    plt.xlabel('Número Total de Investidores', fontsize=12)
    plt.ylabel('País', fontsize=12)

    # Destacar o país com maior número de investidores
    maior_quantidade_investidores = df_investidor_pais.max()
    for i, value in enumerate(df_investidor_pais.values):
        color = 'gold' if value == maior_quantidade_investidores else 'white'
        ax.text(value + 5, i, f'{value:,}', va='center', color=color, fontweight='bold')

    plt.tight_layout()
    
    #Salvar e Exibir Gráfico
    plt.savefig('imagens/Analise_Startup_Pais/Analise_Startup_Pais_QTD_Investidores.png')
    plt.show()

def gerar_tabela_maior_investimento_pais(dados):
    
    #Preparação Dados
    maior_investimento_pais = dados.groupby('Country')['Investment Amount (USD)'].max().sort_values(ascending=False)
    df_maior_investimento = maior_investimento_pais.reset_index()
    df_maior_investimento.columns = ['País', 'Maior Investimento (USD)']
    df_maior_investimento['Maior Investimento (USD)'] = df_maior_investimento['Maior Investimento (USD)'].apply(lambda x: f"${x/1e6:.2f}M")

    total_valor = maior_investimento_pais.sum()
    linha_total = pd.DataFrame([['TOTAL', f"${total_valor/1e6:.2f}M"]], columns=df_maior_investimento.columns)
    df_maior_investimento = pd.concat([df_maior_investimento, linha_total], ignore_index=True)

    #Construção Tabela
    fig, ax = plt.subplots(figsize=(10, len(df_maior_investimento)*0.6))
    ax.axis('off')

    cell_colors = [['#1a3a5f', '#2a4a7f']] * (len(df_maior_investimento)-1) + [['#8a6bd1', '#8a6bd1']]
    table = ax.table(
        cellText=df_maior_investimento.values,
        colLabels=df_maior_investimento.columns,
        cellLoc='center',
        loc='center',
        colColours=['#3a6ea5']*2,
        cellColours=cell_colors
    )

    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.5)

    # Destacar cabeçalho e total
    for (i, j), cell in table.get_celld().items():
        if i == 0 or i == len(df_maior_investimento):
            cell.set_text_props(weight='bold', color='white')
        cell.set_edgecolor('white')

    #Salvar e Exibir Gráfico
    plt.title('Maiores Investimentos por País', fontsize=16, color='white', pad=30)
    plt.tight_layout()
    plt.savefig('imagens/Analise_Startup_Pais/Analise_Startup_Pais_Maior_Valor.png')
    plt.show()

def gerar_grafico_surgimento_startup_anual(dados):
    
    #Preparação Dados
    df_surgimento_startup_anual = dados['Year Founded'].value_counts().sort_index()

    #Construção Gráfico
    plt.figure(figsize=(12, 6))
    ax = sns.lineplot(
        x=df_surgimento_startup_anual.index, 
        y=df_surgimento_startup_anual.values, 
        marker='o', 
        markersize=8,
        linewidth=2.5,
        color='cyan'
    )

    # Configurações do gráfico
    plt.title('Evolução Anual de Fundação de Startups', fontsize=14, pad=20)
    plt.xlabel('Ano', fontsize=12)
    plt.ylabel('Número de Novas Startups', fontsize=12)
    plt.grid(True, alpha=0.3)

    #Salvar e Exibir Gráfico
    plt.tight_layout()
    plt.savefig('imagens/Analise_Startup_Pais/Analise_Startup_Pais_Surgimento_Startup.png')
    plt.show()

def gerar_grafico_distribuicao_segmento_pais(dados):
    
    #Preparação Dados
    df_distribuicao_segmento = pd.crosstab(dados['Country'], dados['Industry'])
    df_distribuicao_segmento = df_distribuicao_segmento.loc[df_distribuicao_segmento.sum(axis=1).sort_values(ascending=False).index]

    #Criação Gráfico

    ax = df_distribuicao_segmento.plot(kind='bar', stacked=True, figsize=(14, 7))

    for bar_index, industry in enumerate(df_distribuicao_segmento.index):
        y_offset = 0
        for stage in df_distribuicao_segmento.columns:
            value = df_distribuicao_segmento.loc[industry, stage]
            if value > 0:
                ax.text(
                    bar_index,
                    y_offset + value / 2,
                    str(value),
                    ha='center',
                    va='center',
                    fontsize=8,
                )
                y_offset += value

    # Personalizar o gráfico
    plt.title('Quantidade de Startups por Segmento em Cada País')
    plt.xlabel('País')
    plt.ylabel('Número de Startups')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Estágio de Investimento', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Mostrar o gráfico
    plt.savefig('imagens/Analise_Startup_Pais/Analise_Startup_Pais_Distribuicao_Segmento.png')
    plt.show()

def gerar_tabela_media_avaliacao_sucesso_pais(dados):
    
    #Preparação Dados
    media_nota_sucesso = dados.groupby('Country')['Success Score'].mean().sort_values(ascending=False)
    df_tabela_media = media_nota_sucesso.reset_index()
    df_tabela_media.columns = ['País', 'Avaliação de Sucesso']

    media_geral = pd.DataFrame([['Média Geral', media_nota_sucesso.mean()]], columns=df_tabela_media.columns)
    df_tabela_media = pd.concat([df_tabela_media, media_geral], ignore_index=True)
    df_tabela_media["Avaliação de Sucesso"] = df_tabela_media["Avaliação de Sucesso"].round(2)

    #Construção Tabela
    fig, ax = plt.subplots(figsize=(10, len(df_tabela_media)*0.6))
    ax.axis('off')

    cell_colors = [['#1a3a5f', '#2a4a7f']] * (len(df_tabela_media)-1) + [['#8a6bd1', '#8a6bd1']]
    table = ax.table(
        cellText=df_tabela_media.values,
        colLabels=df_tabela_media.columns,
        cellLoc='center',
        loc='center',
        colColours=['#3a6ea5']*2,
        cellColours=cell_colors
    )

    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.5)

    # Destacar cabeçalho e total
    for (i, j), cell in table.get_celld().items():
        if i == 0 or i == len(df_tabela_media):
            cell.set_text_props(weight='bold', color='white')
        cell.set_edgecolor('white')

    plt.title('Média Nota de Sucesso', fontsize=16, color='white', pad=30)
    plt.tight_layout()

    #Salvar e Exibir a Imagem
    plt.savefig('imagens/Analise_Startup_Pais/Analise_Startup_Pais_Media_Avaliacao_Sucesso.png')
    plt.show()

def gerar_grafico_estagio_desenvolvimento_pais(dados):
    
    #Preparação Dados

    df_estagio_desenvolvimento = pd.crosstab(dados['Country'], dados['Funding Stage'])
    df_estagio_desenvolvimento = df_estagio_desenvolvimento.loc[df_estagio_desenvolvimento.sum(axis=1).sort_values(ascending=False).index]

    #Construção Tabela
    ax = df_estagio_desenvolvimento.plot(kind='bar', stacked=True, figsize=(14, 7))

    for bar_index, industry in enumerate(df_estagio_desenvolvimento.index):
        y_offset = 0
        for stage in df_estagio_desenvolvimento.columns:
            value = df_estagio_desenvolvimento.loc[industry, stage]
            if value > 0:
                ax.text(
                    bar_index,
                    y_offset + value / 2,
                    str(value),
                    ha='center',
                    va='center',
                    fontsize=8,
                )
                y_offset += value

    plt.title('Quantidade de Startups por Estágio de Investimento em Cada Setor')
    plt.xlabel('País')
    plt.ylabel('Número de Startups')
    plt.xticks(rotation=45, ha='right')
    plt.legend(title='Estágio de Investimento', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Salva E mostra Gráfico
    plt.savefig('imagens/Analise_Startup_Pais/Analise_Startup_Pais_Estagio_Desenvolvimento.png')
    plt.show()

def gerar_analise_startup_pais(dados):
    gerar_grafico_media_de_crescimento(dados)
    gerar_grafico_quantidade_investidores_pais(dados)
    gerar_tabela_maior_investimento_pais(dados)
    gerar_grafico_surgimento_startup_anual(dados)

def gerar_analise_startup_pais_complementar(dados):
    gerar_grafico_estagio_desenvolvimento_pais(dados)
    gerar_grafico_distribuicao_segmento_pais(dados)
    gerar_tabela_media_avaliacao_sucesso_pais(dados)

