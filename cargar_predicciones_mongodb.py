import pandas as pd
from pymongo import MongoClient

print("\n===== CARGA DE PREDICCIONES A MONGODB =====")

# ==========================================
# 1. CARGAR ARCHIVO DE PREDICCIONES
# ==========================================

df = pd.read_csv("prediccion_rendimiento.csv")

print("Archivo de predicciones cargado correctamente.")
print("Total de jugadores:", len(df))


# ==========================================
# 2. CONECTAR CON MONGODB
# ==========================================

cliente = MongoClient("mongodb://localhost:27017/")

# Comprobar que MongoDB responde
cliente.admin.command("ping")

print("Conexion con MongoDB establecida correctamente.")


# ==========================================
# 3. SELECCIONAR BASE DE DATOS
# ==========================================

db = cliente["barcelona_bigdata"]

# Crear / seleccionar colección
coleccion = db["predicciones"]


# ==========================================
# 4. LIMPIAR PREDICCIONES ANTERIORES
# ==========================================

coleccion.delete_many({})

print("Coleccion de predicciones preparada.")


# ==========================================
# 5. CONVERTIR DATAFRAME A DOCUMENTOS
# ==========================================

documentos = df.to_dict("records")


# ==========================================
# 6. INSERTAR PREDICCIONES
# ==========================================

if documentos:
    resultado = coleccion.insert_many(documentos)

    print(
        "Predicciones insertadas:",
        len(resultado.inserted_ids)
    )


# ==========================================
# 7. COMPROBAR INFORMACION
# ==========================================

total = coleccion.count_documents({})

print("\n===== VERIFICACION =====")
print("Documentos almacenados en MongoDB:", total)


# ==========================================
# 8. MOSTRAR EJEMPLO
# ==========================================

ejemplo = coleccion.find_one()

print("\nDocumento de ejemplo:")
print(ejemplo)


# ==========================================
# 9. CERRAR CONEXION
# ==========================================

cliente.close()

print("\nConexion con MongoDB cerrada correctamente.")
print("===== CARGA DE PREDICCIONES TERMINADA =====")