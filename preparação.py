import pandas as pd

# ==========================================
# 1. CARREGAR O DATASET
# ==========================================
df = pd.read_csv("data.csv")

print("Dataset original:")
print(df.shape)

# ==========================================
# 2. REMOVER COLUNA DE ÍNDICE
# ==========================================
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# ==========================================
# 3. VERIFICAR VALORES AUSENTES
# ==========================================
print("\nValores ausentes antes da limpeza:")
print(df.isnull().sum())

# ==========================================
# 4. REMOVER LINHAS COM VALORES AUSENTES
# ==========================================
df = df.dropna()

print("\nDataset após remoção dos valores ausentes:")
print(df.shape)

# ==========================================
# 5. VERIFICAR DUPLICADOS
# ==========================================
print("\nQuantidade de duplicados:")
print(df.duplicated().sum())

# ==========================================
# 6. REMOVER DUPLICADOS
# ==========================================
df = df.drop_duplicates()

# ==========================================
# 7. CONVERTER DURAÇÃO PARA MINUTOS
# ==========================================
df["duration_min"] = df["duration_ms"] / 60000

df = df.drop(columns=["duration_ms"])

# ==========================================
# 8. DEFINIR A VARIÁVEL ALVO (Y)
# ==========================================
y = df["popularity"]

# ==========================================
# 9. DEFINIR AS VARIÁVEIS DE ENTRADA (X)
# ==========================================
colunas_features = [
    "danceability",
    "energy",
    "loudness",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo",
    "duration_min",
    "explicit",
    "track_genre"
]

X = df[colunas_features]

# ==========================================
# 10. MOSTRAR RESULTADO
# ==========================================
print("\n===================================")
print("PREPARAÇÃO CONCLUÍDA!")
print("===================================")

print("\nQuantidade de dados:")
print(df.shape)

print("\nVariável alvo (Y):")
print(y.head())

print("\nVariáveis de entrada (X):")
print(X.head())

print("\nColunas utilizadas:")
print(X.columns.tolist())