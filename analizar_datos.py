import pandas as pd

print("\n===== ANALISIS DE DATOS FC BARCELONA =====")

# ==========================================
# 1. CARGAR DATASET LIMPIO
# ==========================================

df = pd.read_csv("dataset_barcelona_limpio.csv")

print("Dataset cargado correctamente.")
print("Total de registros:", len(df))


# ==========================================
# 2. ANALISIS GENERAL POR JUGADOR
# ==========================================

resumen = df.groupby(["jugador", "posicion"]).agg(
    total_eventos=("evento_id", "count"),
    acciones_exitosas=("resultado_numerico", "sum"),
    acciones_ofensivas=("accion_ofensiva", "sum"),
    partidos=("partido_id", "nunique")
).reset_index()


# ==========================================
# 3. PORCENTAJE DE EXITO
# ==========================================

resumen["porcentaje_exito"] = (
    resumen["acciones_exitosas"] /
    resumen["total_eventos"] * 100
).round(2)


# ==========================================
# 4. CONTAR GOLES, ASISTENCIAS, TIROS,
#    REGATES Y RECUPERACIONES
# ==========================================

acciones = [
    "Gol",
    "Asistencia",
    "Tiro",
    "Regate",
    "Recuperacion"
]

for accion in acciones:

    conteo = (
        df[df["accion"] == accion]
        .groupby("jugador")
        .size()
    )

    resumen[accion.lower()] = (
        resumen["jugador"]
        .map(conteo)
        .fillna(0)
        .astype(int)
    )


# ==========================================
# 5. INDICE DE RENDIMIENTO
# ==========================================

resumen["indice_rendimiento"] = (
    resumen["porcentaje_exito"] * 0.40 +
    (resumen["gol"] / resumen["total_eventos"] * 100) * 0.25 +
    (resumen["asistencia"] / resumen["total_eventos"] * 100) * 0.15 +
    (resumen["acciones_ofensivas"] / resumen["total_eventos"] * 100) * 0.20
).round(2)


# ==========================================
# 6. ORDENAR JUGADORES POR RENDIMIENTO
# ==========================================

resumen = resumen.sort_values(
    by="indice_rendimiento",
    ascending=False
).reset_index(drop=True)


# ==========================================
# 7. MOSTRAR RESULTADOS
# ==========================================

print("\n===== RENDIMIENTO GENERAL POR JUGADOR =====")

print(
    resumen[
        [
            "jugador",
            "posicion",
            "total_eventos",
            "partidos",
            "acciones_exitosas",
            "porcentaje_exito",
            "gol",
            "asistencia",
            "tiro",
            "regate",
            "recuperacion",
            "indice_rendimiento"
        ]
    ].to_string(index=False)
)


# ==========================================
# 8. ANALISIS POR RIVAL
# ==========================================

rendimiento_rival = df.groupby("rival").agg(
    total_eventos=("evento_id", "count"),
    acciones_exitosas=("resultado_numerico", "sum")
).reset_index()

rendimiento_rival["porcentaje_exito"] = (
    rendimiento_rival["acciones_exitosas"] /
    rendimiento_rival["total_eventos"] * 100
).round(2)

rendimiento_rival = rendimiento_rival.sort_values(
    by="porcentaje_exito",
    ascending=False
)

print("\n===== RENDIMIENTO POR RIVAL =====")
print(rendimiento_rival.to_string(index=False))


# ==========================================
# 9. ANALISIS POR TIPO DE ACCION
# ==========================================

acciones_resumen = df.groupby("accion").agg(
    total_acciones=("evento_id", "count"),
    acciones_exitosas=("resultado_numerico", "sum")
).reset_index()

acciones_resumen["porcentaje_exito"] = (
    acciones_resumen["acciones_exitosas"] /
    acciones_resumen["total_acciones"] * 100
).round(2)

acciones_resumen = acciones_resumen.sort_values(
    by="total_acciones",
    ascending=False
)

print("\n===== ANALISIS POR TIPO DE ACCION =====")
print(acciones_resumen.to_string(index=False))


# ==========================================
# 10. GUARDAR RESULTADOS PARA POWER BI
# ==========================================

resumen.to_csv(
    "rendimiento_jugadores.csv",
    index=False
)

rendimiento_rival.to_csv(
    "rendimiento_rivales.csv",
    index=False
)

acciones_resumen.to_csv(
    "rendimiento_acciones.csv",
    index=False
)


# ==========================================
# 11. FINALIZAR
# ==========================================

print("\n===== ANALISIS TERMINADO =====")
print("Archivos generados:")
print("- rendimiento_jugadores.csv")
print("- rendimiento_rivales.csv")
print("- rendimiento_acciones.csv")