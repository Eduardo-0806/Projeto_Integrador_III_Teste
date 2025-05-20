import matplotlib.pyplot as plt
import pandas as pd


df_startup = pd.read_csv("startup_growth_investment_data.csv", delimiter=",")
print(df_startup.columns)

#Gráfico de Soma de Valor Estimado por Segmento

series_valorizacao_segmento = df_startup.groupby("Industry")["Valuation (USD)"].sum()
series_valorizacao_segmento = (series_valorizacao_segmento / 1000000000000).round(3)
series_valorizacao_segmento.sort_values(ascending= False, inplace=True)

plt.bar(series_valorizacao_segmento.index,series_valorizacao_segmento.values)
plt.title("Soma de Valor Estimado por Segmento", fontsize=12, fontweight='bold', pad=10)
plt.ylabel("Valor (USD)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("img\\Figura_1.png")
plt.show()


#Gráfico de Total de Investimento em Startup Por Ano

series_total_investimento = df_startup.groupby("Year Founded")["Investment Amount (USD)"].sum()
series_total_investimento = (series_total_investimento / 1000000000000).round(3)

plt.plot(series_total_investimento)
plt.title("Total de Investimento em Startup Por Ano", fontsize=12, fontweight='bold', pad=10)
plt.ylabel("Valor (USD)")
plt.savefig("img\\Figura_2.png")
plt.show()


#Gráfico de QTD de Startup por Segmento

quantidade = df_startup["Industry"].value_counts()
porcentagem = (df_startup["Industry"].value_counts(normalize=True) * 100).round(2)

df_quantidade_startup = pd.DataFrame({"Segmento": quantidade.index, "Quantidade": quantidade.values, "%": porcentagem.values})
df_quantidade_startup.sort_values(by="Quantidade", ascending=False, inplace=True)
df_quantidade_startup.loc[len(df_quantidade_startup)] = {"Segmento": "Total", "Quantidade": sum(quantidade.values), 
                                                         "%": sum(porcentagem.values)}
print(df_quantidade_startup)

fig, ax = plt.subplots(figsize=(6, 4))
ax.axis('off')

# Criar a tabela
table = ax.table(
    cellText=df_quantidade_startup.values,
    colLabels=df_quantidade_startup.columns,
    cellLoc='center',
    loc='center'
)

# Estilo da tabela
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

# Cabeçalho
n_rows = len(df_quantidade_startup)
print(n_rows)
for (row, col), cell in table.get_celld().items():
    if row == 0:  # Cabeçalho
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#3366CC')
    elif row > 0 and row < n_rows:  # Linhas normais
        cell.set_facecolor('#E6F0FF')
    elif row == n_rows:  # Linha Total
        cell.set_facecolor('#CCE0FF')

# Título
plt.title("QTD de Startup por Segmento", fontsize=12, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig("img\\Figura_3.png")
plt.show()


#Valor Investidor por Segmento

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

print(df_investimento_por_segmento)

fig, ax = plt.subplots(figsize=(6, 4))
ax.axis('off')

# Criar a tabela
table = ax.table(
    cellText=df_investimento_por_segmento.values,
    colLabels=df_investimento_por_segmento.columns,
    cellLoc='center',
    loc='center'
)

# Estilo da tabela
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

# Cabeçalho
n_rows = len(df_investimento_por_segmento)
print(n_rows)
for (row, col), cell in table.get_celld().items():
    if row == 0:  # Cabeçalho
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#3366CC')
    elif row > 0 and row < n_rows:  # Linhas normais
        cell.set_facecolor('#E6F0FF')
    elif row == n_rows:  # Linha Total
        cell.set_facecolor('#CCE0FF')

# Título
plt.title("Valor Investidor por Segmento", fontsize=12, fontweight='bold', pad=10)
plt.tight_layout()
plt.savefig("img\\Figura_4.png")
plt.show()
