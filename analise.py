import matplotlib.pyplot as plt
import pandas as pd
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

# Importação dos DataSet
df_startup = pd.read_csv("startup_growth_investment_data.csv", delimiter=",")
df_perfil = pd.read_csv("Original_data.csv")

#Configurações Gerais Gráficos
plt.rcParams['axes.facecolor'] = '#5a8dc4'
plt.rcParams['figure.facecolor'] = '#5a8dc4'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.edgecolor'] = 'white'

#               ANALISE DE STARTUP POR PAIS

# ======================================
# 1. Soma de Valor Estimado por Segmento
# ======================================

#Preparação Dados

series_valorizacao_segmento = df_startup.groupby("Industry")["Valuation (USD)"].sum()
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
#plt.savefig("img\\Analise_Startup_Pais_Soma_Valorizacao")
plt.show()

# ======================================
# 2. Total de Investimento Por Ano
# ======================================

#Preparação Dados

series_total_investimento = df_startup.groupby("Year Founded")["Investment Amount (USD)"].sum()
series_total_investimento = (series_total_investimento / 1000000000000).round(3)

#Criação Gráfico
plt.plot(series_total_investimento, color="cyan")
plt.title("Total de Investimento em Startup Por Ano", fontsize=12, fontweight='bold', pad=10)
plt.ylabel("Valor (USD)")
#plt.savefig("img\\Analise_Startup_Pais_Total_Investimento")
plt.show()

# ======================================
# 3. Quantidade de Startup por Segmento
# ======================================

#Preparação Dados

quantidade = df_startup["Industry"].value_counts()
porcentagem = (df_startup["Industry"].value_counts(normalize=True) * 100).round(2)

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
plt.title("Valor Investido por Segmento", fontsize=14, fontweight='bold', color='white', pad=20)
#plt.savefig("img\\Analise_Startup_Pais_QTD")
plt.show()

# ======================================
# 4. Valor Investido por Segmento
# ======================================

#Preparação Dados

soma_valores = df_startup.groupby("Industry")["Investment Amount (USD)"].sum()
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

table = ax.table(
    cellText=df_investimento_por_segmento.values,
    colLabels=df_investimento_por_segmento.columns,
    cellLoc='center',
    loc='center',
    colColours=['#3a6ea5'] * 3,
    cellColours=cell_colors
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
plt.savefig("img\\Analise_Startup_Pais_Valor_Investido")
plt.show()

#               ANALISE DE STARTUP POR SEGMENTO 

# ======================================
# 1. MÉDIA DE CRESCIMENTO POR PAÍS
# ======================================

#Preparação dos Dados

growth_by_country = df_startup.groupby('Country')['Growth Rate (%)'].mean().sort_values(ascending=False)

# Construção do gráfico
plt.figure(figsize=(12, 8))
ax = sns.barplot(x=growth_by_country.values, y=growth_by_country.index, palette='Blues_r')
plt.title('Média de Porcentagem de Crescimento por País\n(Ordenado por Desempenho)', fontsize=14, pad=20)
plt.xlabel('Média de Crescimento (%)', fontsize=12)
plt.ylabel('País', fontsize=12)

# Adicionar valores nas barras
for i, value in enumerate(growth_by_country.values):
    ax.text(value + 0.5, i, f'{value:.1f}%', va='center', color='white', fontweight='bold')

plt.tight_layout()
#dpi=300, bbox_inches='tight'
plt.savefig('img/Analise_Startup_Segmento_Crescimento.png')
plt.show()

# ======================================
# 2. QUANTIDADE DE INVESTIDORES POR PAÍS
# ======================================

#Preparação Dados

plt.figure(figsize=(12, 8))
investors_by_country = df_startup.groupby('Country')['Number of Investors'].sum().sort_values(ascending=False)

# Construção Gráfico
ax = sns.barplot(x=investors_by_country.values, y=investors_by_country.index, palette='Blues_r')
plt.title('Total de Investidores por País\n(Ordenado por Volume)', fontsize=14, pad=20)
plt.xlabel('Número Total de Investidores', fontsize=12)
plt.ylabel('País', fontsize=12)

# Destacar o país com maior número de investidores
max_investors = investors_by_country.max()
for i, value in enumerate(investors_by_country.values):
    color = 'gold' if value == max_investors else 'white'
    ax.text(value + 5, i, f'{value:,}', va='center', color=color, fontweight='bold')

plt.tight_layout()
plt.savefig('img/Analise_Startup_Segmento_QTD_Investidores.png')
plt.show()

# ======================================
# 3. MAIOR VALOR INVESTIDO POR PAÍS (TABELA)
# ======================================

#Preparação Dados

max_invest_by_country = df_startup.groupby('Country')['Investment Amount (USD)'].max().sort_values(ascending=False)
table_df_startup = max_invest_by_country.reset_index()
table_df_startup.columns = ['País', 'Maior Investimento (USD)']
table_df_startup['Maior Investimento (USD)'] = table_df_startup['Maior Investimento (USD)'].apply(lambda x: f"${x/1e6:.2f}M")

total_valor = max_invest_by_country.sum()
print(f"Valor calculado para TOTAL/MÉDIA: ${total_valor:,.2f}")
total_row = pd.DataFrame([['TOTAL', f"${total_valor/1e6:.2f}M"]], columns=table_df_startup.columns)
table_df_startup = pd.concat([table_df_startup, total_row], ignore_index=True)

#Construção Tabela

fig, ax = plt.subplots(figsize=(10, len(table_df_startup)*0.6))
ax.axis('off')

cell_colors = [['#1a3a5f', '#2a4a7f']] * (len(table_df_startup)-1) + [['#8a6bd1', '#8a6bd1']]
table = ax.table(
    cellText=table_df_startup.values,
    colLabels=table_df_startup.columns,
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
    if i == 0 or i == len(table_df_startup):
        cell.set_text_props(weight='bold', color='white')
    cell.set_edgecolor('white')

plt.title('Maiores Investimentos por País', fontsize=16, color='white', pad=30)
plt.tight_layout()
plt.savefig('img/Analise_Startup_Segmento_Maior_Valor.png')
plt.show()

# ======================================
# 4. SURGIMENTO DE STARTUPS POR ANO
# ======================================

#Preparação Dados

startups_by_year = df_startup['Year Founded'].value_counts().sort_index()

#Construção Gráfico

plt.figure(figsize=(12, 6))
ax = sns.lineplot(
    x=startups_by_year.index, 
    y=startups_by_year.values, 
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

plt.tight_layout()
plt.savefig('img/Analise_Startup_Segmento_Surgimento_Startup.png')
plt.show()

print("\nAnálise concluída! Gráficos salvos no diretório atual.")

#               ANALISE DE PERFIL 

# ======================================
# 1. Distribuição de Gênero
# ======================================

fig, ax = plt.subplots()

#Preparação Dados

genero_counts = df_perfil['GENDER'].value_counts()
labels = genero_counts.index
sizes = genero_counts.values

#Construção Gráfico 

ax.pie(sizes, labels=[f"{l}\n({v} - {v/sum(sizes)*100:.1f}%)" for l, v in zip(labels, sizes)],
       colors=['#5dade2', '#ec407a'], startangle=90)
ax.set_title('Distribuição de Gênero')
plt.savefig("img/Analise_Perfil_Genero.png")
plt.show()

# ======================================
# 2. Distribuição por Faixa Etária
# ======================================

fig, ax = plt.subplots()

#Preparação Dados

df_perfil['AGE'] = pd.to_numeric(df_perfil['AGE'], errors='coerce')
df_perfil['Faixa Etária'] = df_perfil['AGE'].apply(categorizar_idade)

faixas_ordenadas = ['25-30', '30-35', '20-25']
faixa_counts = df_perfil['Faixa Etária'].value_counts()
faixa_counts = faixa_counts.reindex(faixas_ordenadas).fillna(0).astype(int)

cores_faixa = ['#4dabf7', '#1e3d59', '#a3d5f7']
labels = faixa_counts.index
sizes = faixa_counts.values

#Construção Gráfico

ax.pie(sizes, labels=[f"{v}\n({v/sum(sizes)*100:.0f}%)" for v in sizes],
       colors=cores_faixa, startangle=90)
ax.legend(labels, title="Faixa Etária", loc="center left",
          bbox_to_anchor=(1, 0.5), fontsize=10)
ax.set_title('Distribuição Faixa Etária')
plt.savefig("img/Analise_Perfil_Faixa_Etaria.png")
plt.show()

# ======================================
# 3. Expectativa de Retorno
# ======================================

fig, ax = plt.subplots()

#Preparação Dados

objetivos_counts = df_perfil['What is your investment objective?'].value_counts()
labels = objetivos_counts.index
sizes = objetivos_counts.values

#Construção Gráfico

ax.pie(sizes, labels=[f"{l}\n({v} - {v/sum(sizes)*100:.1f}%)" for l, v in zip(labels, sizes)],
       colors=cores_faixa, startangle=90)
ax.set_title('Objetivo do Investimento')
plt.savefig("img/Analise_Perfil_Expectativa_Retorno.png")

plt.show()

# ======================================
# 4. Objetivo de Investimento
# ======================================

fig, ax = plt.subplots()

#Preparação Dados

retorno_counts = df_perfil['How much return do you expect from any investment instrument?'].value_counts()

#Construção Gráfico

sns.barplot(y=retorno_counts.index, x=retorno_counts.values,
            ax=ax, palette='Blues_r')
ax.set_title('Expectativa de Retorno')
ax.set_xlabel('QTD')
ax.set_ylabel('Retorno Esperado')

plt.savefig("img/Analise_Perfil_Objetivo.png")
plt.show()

# ======================================
# 5. Fonte de Informação
# ======================================

fig, ax = plt.subplots()

#Preparação Dados

fonte_counts = df_perfil['Your sources of information for investments is '].value_counts()

#Construção Gráfico

sns.barplot(x=fonte_counts.index, y=fonte_counts.values,
            ax=ax, palette='Blues')
ax.set_title('Fontes de Informação')
ax.set_ylabel('QTD')
ax.set_xlabel('Fonte')
ax.tick_params(axis='x', rotation=25)

plt.tight_layout()
plt.savefig("img/Analise_Perfil_Fonte_Informacao.png")

plt.show()