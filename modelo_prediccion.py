import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

print("\n===== MODELO DE PREDICCION FC BARCELONA =====")

# ==========================================
# 1. CARGAR DATOS DE RENDIMIENTO
# ==========================================

df = pd.read_csv("rendimiento_jugadores.csv")

print("Datos cargados correctamente.")
print("Jugadores disponibles:", len(df))


# ==========================================
# 2. VARIABLES PARA EL MODELO
# ==========================================

variables = [
    "total_eventos",
    "partidos",
    "acciones_exitosas",
    "porcentaje_exito",
    "gol",
    "asistencia",
    "tiro",
    "regate",
    "recuperacion"
]

X = df[variables]

# Variable que queremos predecir
y = df["indice_rendimiento"]


# ==========================================
# 3. DIVIDIR DATOS
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

print("\nDatos para entrenamiento:", len(X_train))
print("Datos para prueba:", len(X_test))


# ==========================================
# 4. CREAR MODELO RANDOM FOREST
# ==========================================

modelo = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

modelo.fit(X_train, y_train)

print("\nModelo entrenado correctamente.")


# ==========================================
# 5. REALIZAR PREDICCIONES
# ==========================================

predicciones = modelo.predict(X_test)

mae = mean_absolute_error(y_test, predicciones)
r2 = r2_score(y_test, predicciones)

print("\n===== EVALUACION DEL MODELO =====")
print("Error absoluto medio (MAE):", round(mae, 4))
print("Coeficiente R2:", round(r2, 4))


# ==========================================
# 6. PREDECIR RENDIMIENTO DE TODOS
#    LOS JUGADORES
# ==========================================

df["rendimiento_predicho"] = modelo.predict(X)

df["diferencia_prediccion"] = (
    df["rendimiento_predicho"] -
    df["indice_rendimiento"]
).round(2)

df["rendimiento_predicho"] = (
    df["rendimiento_predicho"].round(2)
)


# ==========================================
# 7. ORDENAR RESULTADOS
# ==========================================

df = df.sort_values(
    by="rendimiento_predicho",
    ascending=False
).reset_index(drop=True)


# ==========================================
# 8. MOSTRAR PREDICCIONES
# ==========================================

print("\n===== PREDICCION DE RENDIMIENTO =====")

print(
    df[
        [
            "jugador",
            "posicion",
            "indice_rendimiento",
            "rendimiento_predicho",
            "diferencia_prediccion"
        ]
    ].to_string(index=False)
)


# ==========================================
# 9. GUARDAR RESULTADOS
# ==========================================

df.to_csv(
    "prediccion_rendimiento.csv",
    index=False
)

print("\nArchivo generado: prediccion_rendimiento.csv")
print("\n===== MODELO DE PREDICCION TERMINADO =====")