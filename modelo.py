import matplotlib

# Evita erros do Tkinter ao gerar gráficos sem abrir janelas
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.ticker import PercentFormatter
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


# ==========================================
# 1. CARREGAR E PREPARAR O DATASET
# ==========================================

df = pd.read_csv("data.csv")

# Remover coluna de índice, caso exista
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# Remover valores ausentes e duplicados
df = df.dropna()
df = df.drop_duplicates()

# Converter duração de milissegundos para minutos
df["duration_min"] = df["duration_ms"] / 60000

# Remover coluna original
df = df.drop(columns=["duration_ms"])


# ==========================================
# 2. DEFINIR VARIÁVEL ALVO
# ==========================================

y = df["popularity"]


# ==========================================
# 3. DEFINIR FEATURES
# ==========================================

features = [
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

X = df[features].copy()


# ==========================================
# 4. TRANSFORMAR EXPLICIT EM NÚMERO
# ==========================================

X["explicit"] = X["explicit"].astype(int)


# ==========================================
# 5. DIVIDIR EM TREINO E TESTE
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n===================================")
print("DIVISÃO DOS DADOS")
print("===================================")
print("Dados para treinamento:", X_train.shape)
print("Dados para teste:", X_test.shape)


# ==========================================
# 6. FEATURES NUMÉRICAS
# ==========================================

features_numericas = [
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
    "explicit"
]


# ==========================================
# 7. PRÉ-PROCESSAMENTO COM GÊNERO
# ==========================================

preprocessador_com_genero = ColumnTransformer(
    transformers=[
        (
            "genero",
            OneHotEncoder(handle_unknown="ignore"),
            ["track_genre"]
        )
    ],
    remainder="passthrough"
)


# ==========================================
# 8. PRÉ-PROCESSAMENTO SEM GÊNERO
# ==========================================

preprocessador_sem_genero = ColumnTransformer(
    transformers=[
        (
            "numericas",
            "passthrough",
            features_numericas
        )
    ]
)


# ==========================================
# 9. REGRESSÃO LINEAR + GÊNERO
# ==========================================

modelo_linear_genero = Pipeline(
    steps=[
        ("preprocessamento", preprocessador_com_genero),
        ("modelo", LinearRegression())
    ]
)


# ==========================================
# 10. RANDOM FOREST + GÊNERO
# ==========================================

modelo_rf_genero = Pipeline(
    steps=[
        ("preprocessamento", preprocessador_com_genero),
        (
            "modelo",
            RandomForestRegressor(
                n_estimators=50,
                random_state=42,
                n_jobs=-1
            )
        )
    ]
)


# ==========================================
# 11. REGRESSÃO LINEAR SEM GÊNERO
# ==========================================

modelo_linear_sem_genero = Pipeline(
    steps=[
        ("preprocessamento", preprocessador_sem_genero),
        ("modelo", LinearRegression())
    ]
)


# ==========================================
# 12. RANDOM FOREST SEM GÊNERO
# ==========================================

modelo_rf_sem_genero = Pipeline(
    steps=[
        ("preprocessamento", preprocessador_sem_genero),
        (
            "modelo",
            RandomForestRegressor(
                n_estimators=50,
                random_state=42,
                n_jobs=-1
            )
        )
    ]
)


# ==========================================
# 13. FUNÇÃO PARA AVALIAR OS MODELOS
# ==========================================

def avaliar_modelo(nome, modelo):
    print("\n===================================")
    print(nome)
    print("===================================")

    print("Treinando modelo...")
    modelo.fit(X_train, y_train)

    print("Modelo treinado!")
    print("Realizando previsões...")

    previsoes = modelo.predict(X_test)

    mae = mean_absolute_error(y_test, previsoes)
    rmse = np.sqrt(mean_squared_error(y_test, previsoes))
    r2 = r2_score(y_test, previsoes)

    print("MAE:", round(mae, 2))
    print("RMSE:", round(rmse, 2))
    print("R²:", round(r2, 2))

    resultados = {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }

    return modelo, resultados


# ==========================================
# 14. TREINAR E AVALIAR OS MODELOS
# ==========================================

modelo_linear_genero, resultado_linear_genero = avaliar_modelo(
    "REGRESSÃO LINEAR + GÊNERO",
    modelo_linear_genero
)

modelo_rf_genero, resultado_rf_genero = avaliar_modelo(
    "RANDOM FOREST + GÊNERO",
    modelo_rf_genero
)

modelo_linear_sem_genero, resultado_linear_sem_genero = avaliar_modelo(
    "REGRESSÃO LINEAR SEM GÊNERO",
    modelo_linear_sem_genero
)

modelo_rf_sem_genero, resultado_rf_sem_genero = avaliar_modelo(
    "RANDOM FOREST SEM GÊNERO",
    modelo_rf_sem_genero
)


# ==========================================
# 15. FINAL DO TREINAMENTO
# ==========================================

print("\n===================================")
print("TREINAMENTO CONCLUÍDO!")
print("===================================")


# ==========================================
# 16. RESULTADOS DOS MODELOS
# ==========================================

modelos = [
    "Regressão Linear\n+ Gênero",
    "Random Forest\n+ Gênero",
    "Regressão Linear\nSem Gênero",
    "Random Forest\nSem Gênero"
]

resultados_modelos = [
    resultado_linear_genero,
    resultado_rf_genero,
    resultado_linear_sem_genero,
    resultado_rf_sem_genero
]

mae_resultados = [resultado["MAE"] for resultado in resultados_modelos]
rmse_resultados = [resultado["RMSE"] for resultado in resultados_modelos]
r2_resultados = [resultado["R2"] for resultado in resultados_modelos]


# ==========================================
# 17. GRÁFICO - MAE
# ==========================================

plt.figure(figsize=(10, 6))
plt.bar(modelos, mae_resultados, color="steelblue")

plt.title("Comparação do MAE entre os modelos")
plt.xlabel("Modelo")
plt.ylabel("MAE")

plt.tight_layout()
plt.savefig(
    "grafico_mae.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ==========================================
# 18. GRÁFICO - RMSE
# ==========================================

plt.figure(figsize=(10, 6))
plt.bar(modelos, rmse_resultados, color="darkorange")

plt.title("Comparação do RMSE entre os modelos")
plt.xlabel("Modelo")
plt.ylabel("RMSE")

plt.tight_layout()
plt.savefig(
    "grafico_rmse.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ==========================================
# 19. GRÁFICO - R²
# ==========================================

plt.figure(figsize=(10, 6))
plt.bar(modelos, r2_resultados, color="seagreen")

plt.title("Comparação do R² entre os modelos")
plt.xlabel("Modelo")
plt.ylabel("R²")

plt.tight_layout()
plt.savefig(
    "grafico_r2.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ==========================================
# 20. IMPORTÂNCIA DAS VARIÁVEIS
# ==========================================

print("\n===================================")
print("IMPORTÂNCIA DAS VARIÁVEIS")
print("===================================")

# Análise da Random Forest sem gênero
preprocessador = modelo_rf_sem_genero.named_steps["preprocessamento"]
modelo_rf = modelo_rf_sem_genero.named_steps["modelo"]

nomes_features = preprocessador.get_feature_names_out()
importancias = modelo_rf.feature_importances_

importancia_df = pd.DataFrame({
    "Variavel": nomes_features,
    "Importancia": importancias
})

# Remove o prefixo gerado pelo pré-processador
importancia_df["Variavel"] = importancia_df["Variavel"].str.replace(
    "numericas__",
    "",
    regex=False
)

importancia_df = importancia_df.sort_values(
    by="Importancia",
    ascending=False
)

print(importancia_df.to_string(index=False))


# ==========================================
# 21. GRÁFICO DAS VARIÁVEIS MAIS IMPORTANTES
# ==========================================

top_10 = importancia_df.head(10).sort_values(
    by="Importancia",
    ascending=True
)

plt.figure(figsize=(10, 6))

barras = plt.barh(
    top_10["Variavel"],
    top_10["Importancia"],
    color="mediumpurple"
)

plt.title("10 variáveis mais importantes para a Random Forest")
plt.xlabel("Importância (%)")
plt.ylabel("Variável")

plt.gca().xaxis.set_major_formatter(PercentFormatter(1.0))

for barra, valor in zip(barras, top_10["Importancia"]):
    plt.text(
        barra.get_width() + 0.002,
        barra.get_y() + barra.get_height() / 2,
        f"{valor:.2%}",
        va="center"
    )

plt.tight_layout()
plt.savefig(
    "importancia_variaveis.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()


# ==========================================
# 22. FINAL
# ==========================================

print("\n===================================")
print("ANÁLISE CONCLUÍDA!")
print("===================================")

print("Gráficos gerados:")
print("- grafico_mae.png")
print("- grafico_rmse.png")
print("- grafico_r2.png")
print("- importancia_variaveis.png")