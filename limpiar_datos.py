import pandas as pd

# Cargar el dataset generado
print("Cargando dataset...")

df = pd.read_csv("dataset_barcelona.csv")

print("Dataset cargado correctamente.")
print("Registros originales:", len(df))


# 1. Revisar valores nulos
print("\nValores nulos encontrados:")
print(df.isnull().sum())


# 2. Eliminar registros duplicados
duplicados = df.duplicated().sum()

print("\nRegistros duplicados encontrados:", duplicados)

df = df.drop_duplicates()


# 3. Eliminar registros con valores nulos
df = df.dropna()


# 4. Validar que los minutos esten entre 1 y 90
df = df[
    (df["minuto"] >= 1) &
    (df["minuto"] <= 90)
]


# 5. Crear una columna numerica para el resultado
df["resultado_numerico"] = df["resultado"].map({
    "Exitoso": 1,
    "Fallido": 0
})


# 6. Crear indicador de acciones ofensivas
df["accion_ofensiva"] = df["accion"].isin([
    "Tiro",
    "Regate",
    "Asistencia",
    "Gol"
]).astype(int)


# 7. Guardar el dataset limpio
df.to_csv(
    "dataset_barcelona_limpio.csv",
    index=False
)


# Mostrar resultados
print("\nLimpieza terminada correctamente.")
print("Registros finales:", len(df))

print("\nPrimeros 10 registros:")
print(df.head(10))

print(
    "\nDataset limpio guardado como "
    "dataset_barcelona_limpio.csv"
)