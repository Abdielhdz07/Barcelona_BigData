from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    count,
    sum,
    avg,
    round
)

# Crear sesion de Spark
spark = SparkSession.builder \
    .appName("Barcelona Big Data") \
    .master("local[*]") \
    .getOrCreate()

# Reducir mensajes de Spark en la terminal
spark.sparkContext.setLogLevel("ERROR")

print("\n===== PROCESAMIENTO CON APACHE SPARK =====")

# Cargar el dataset limpio
df = spark.read.csv(
    "dataset_barcelona_limpio.csv",
    header=True,
    inferSchema=True
)

# Contar registros
total_registros = df.count()

print("\nDataset cargado correctamente en Spark.")
print("Total de registros procesados:", total_registros)

# Mostrar estructura del dataset
print("\nEstructura del dataset:")
df.printSchema()

# Analizar rendimiento por jugador
print("\n===== RENDIMIENTO POR JUGADOR =====")

rendimiento_jugadores = df.groupBy(
    "jugador"
).agg(
    count("*").alias("total_eventos"),
    sum("resultado_numerico").alias("acciones_exitosas"),
    sum("accion_ofensiva").alias("acciones_ofensivas"),
    round(
        avg("resultado_numerico") * 100,
        2
    ).alias("porcentaje_exito")
).orderBy(
    "porcentaje_exito",
    ascending=False
)

rendimiento_jugadores.show(
    20,
    truncate=False
)

# Analizar tipos de acciones
print("\n===== ACCIONES REALIZADAS =====")

acciones = df.groupBy(
    "accion"
).count().orderBy(
    "count",
    ascending=False
)

acciones.show(
    20,
    truncate=False
)

# Analizar rendimiento contra rivales
print("\n===== RENDIMIENTO POR RIVAL =====")

rendimiento_rivales = df.groupBy(
    "rival"
).agg(
    count("*").alias("total_eventos"),
    round(
        avg("resultado_numerico") * 100,
        2
    ).alias("porcentaje_exito")
).orderBy(
    "porcentaje_exito",
    ascending=False
)

rendimiento_rivales.show(
    20,
    truncate=False
)

# Guardar resultados del procesamiento
rendimiento_jugadores.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("resultados_spark")

print("\nProcesamiento con Spark terminado correctamente.")
print("Resultados guardados en la carpeta: resultados_spark")

# Cerrar Spark
spark.stop()