import pandas as pd
from pymongo import MongoClient

# Conexion con MongoDB local
cliente = MongoClient("mongodb://localhost:27017/")

# Comprobar conexion
cliente.admin.command("ping")

print("Conexion con MongoDB realizada correctamente.")

# Crear o seleccionar la base de datos
db = cliente["barcelona_bigdata"]

# Crear o seleccionar la coleccion
coleccion = db["eventos"]

# Eliminar datos anteriores de la coleccion
coleccion.delete_many({})

print("Base de datos: barcelona_bigdata")
print("Coleccion: eventos")

# Leer el dataset limpio por bloques
tamano_bloque = 10000
total_insertados = 0

print("\nIniciando carga de datos...")

for bloque in pd.read_csv(
    "dataset_barcelona_limpio.csv",
    chunksize=tamano_bloque
):
    registros = bloque.to_dict("records")

    coleccion.insert_many(registros)

    total_insertados += len(registros)

    print(
        "Registros insertados:",
        total_insertados
    )

# Comprobar cantidad almacenada
total_mongodb = coleccion.count_documents({})

print("\n===== CARGA TERMINADA =====")
print("Registros insertados en MongoDB:", total_mongodb)

# Mostrar un documento de ejemplo
print("\nDocumento de ejemplo:")
print(coleccion.find_one())

# Cerrar conexion
cliente.close()

print("\nConexion con MongoDB cerrada correctamente.")