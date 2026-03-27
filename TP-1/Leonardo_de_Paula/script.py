import pandas as pd
import numpy as np

# =========================
# 1. Carregar os dados
# =========================
file_path = "API_SE.PRM.CMPT.FE.ZS_DS2_en_csv_v2_8339.csv"

df = pd.read_csv(file_path, skiprows=4)

# Visualizar estrutura inicial
print(df.head())

# =========================
# 2. Remover colunas desnecessárias
# =========================
df = df.drop(columns=["Indicator Name", "Indicator Code"], errors='ignore')

# =========================
# 3. Identificar colunas de anos
# =========================
year_columns = [col for col in df.columns if col.isdigit()]

# =========================
# 4. Converter para formato numérico
# =========================
df[year_columns] = df[year_columns].apply(pd.to_numeric, errors='coerce')

# =========================
# 5. Tratar inconsistências
# =========================
# Valores inválidos: <0 ou >100
df[year_columns] = df[year_columns].applymap(
    lambda x: np.nan if (x is not None and (x < 0 or x > 100)) else x
)

# =========================
# 6. Preencher dados faltantes
# =========================

# Estratégia 1: interpolação ao longo dos anos
df[year_columns] = df[year_columns].interpolate(
    axis=1, limit_direction='both'
)

# Estratégia 2 (backup): preencher com média do país
df[year_columns] = df[year_columns].apply(
    lambda row: row.fillna(row.mean()), axis=1
)

# =========================
# 7. Remover países sem dados suficientes
# =========================
df = df.dropna(thresh=int(len(year_columns) * 0.5))

# =========================
# 8. Resetar índice
# =========================
df = df.reset_index(drop=True)

# =========================
# 9. Verificação final
# =========================
print("\nResumo após limpeza:")
print(df.describe())

# =========================
# 10. Salvar dataset limpo
# =========================
df.to_csv("dados_limpos_educacao_feminina.csv", index=False)