# Neste arquivo Python serão realizadas as instruções da Segunda Etapa, as quais serão descritas a seguir

# IDENTIFICAR DADOS FALTANTES
# Carregando e corrigindo estruturas (Subtópico para melhorar os dados)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("escolaridade.csv", sep=";", skiprows=6)

print(df.head())
print(df.columns)

# Fim do subtópico

print(df.isnull().sum())

# CORRIGINDO INCONSISTÊNCIAS

df.replace("-", pd.NA, inplace=True)
for col in df.columns [3:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df.columns = [
    "Regiao", "Cor", "Idade",
    "Total_geral", "Homens_total", "Mulheres_total",
    "Fund_inc", "Homens_fund_inc", "Mulheres_fund_inc",
    "Fund_comp", "Homens_fund_comp", "Mulheres_fund_comp",
    "Med_sup", "Homens_med_sup", "Mulheres_med_sup"
]

# PADRONIZAÇÃO DE VARIÁVEIS

df["Cor"] = df["Cor"].str.strip().str.lower()
df["Regiao"] = df["Regiao"].str.strip()
df["Cor"] = df["Cor"].str.capitalize()

# Verificando inconsistências lógicas (Subtópico)

print((df["Total_geral"] != df["Homens_total"] + df["Mulheres_total"]).sum())

# PREPARANDO DADOS PARA ANÁLISE

df["prop_homens"] = df["Homens_total"] / df["Total_geral"]
df_total = df[df["Idade"] == "Total"]

# ANALISANDO ATRAVÉS DE GRÁFICOS

# Gráfico 1: Escolaridade por raça/cor

df_cor = df_total.groupby("Cor")["Med_sup"].mean()
plt.figure()
df_cor.plot(kind="bar")
plt.title("Escolaridade por raça/cor")
plt.xlabel("Cor/Raça")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.show()

# Gráfico 2: Comparação entre homens e mulheres

df_sexo = df[df["Idade"] == "Total"]
media_homens = df_sexo["Homens_med_sup"].mean()
media_mulheres = df_sexo["Mulheres_med_sup"].mean()
plt.figure()
plt.bar(["Homens", "Mulheres"], [media_homens, media_mulheres])
plt.title("Escolaridade por sexo")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.show()

# Gráfico 3: Escolaridade por Região

df_regiao = df[df["Idade"] == "Total"].groupby("Regiao")["Med_sup"].mean()
plt.figure()
df_regiao.plot(kind="bar")
plt.title("Média de pessoas com ensino médio completo/superior incompleto por região")
plt.xlabel("Região")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.show()

# Gráfico 4: Jovens vs escolaridade 

df_jovens = df[df["Idade"].isin(["15 a 19 anos", "20 a 24 anos"])]
df_jovens.groupby("Idade")["Med_sup"].mean().plot(kind="bar")
plt.title("Escolaridade entre jovens")
plt.ylabel("Quantidade")
plt.xticks(rotation=45)
plt.show()


 