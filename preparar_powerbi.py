import pandas as pd

print("\n===== PREPARACION DE DATOS PARA POWER BI =====")

# ============================================
# 1. CARGAR ARCHIVOS
# ============================================

jugadores = pd.read_csv("prediccion_rendimiento.csv")
rivales = pd.read_csv("rendimiento_rivales.csv")
acciones = pd.read_csv("rendimiento_acciones.csv")

print("Archivos cargados correctamente.")


# ============================================
# 2. PREPARAR DATOS DE JUGADORES
# ============================================

columnas_jugadores = [
    "jugador",
    "posicion",
    "total_eventos",
    "acciones_exitosas",
    "acciones_ofensivas",
    "partidos",
    "porcentaje_exito",
    "gol",
    "asistencia",
    "tiro",
    "regate",
    "recuperacion",
    "indice_rendimiento",
    "rendimiento_predicho",
    "diferencia_prediccion"
]

columnas_disponibles = [
    columna
    for columna in columnas_jugadores
    if columna in jugadores.columns
]

dashboard_jugadores = jugadores[columnas_disponibles].copy()

# Ordenar por rendimiento predicho
if "rendimiento_predicho" in dashboard_jugadores.columns:
    dashboard_jugadores = dashboard_jugadores.sort_values(
        by="rendimiento_predicho",
        ascending=False
    )


# ============================================
# 3. PREPARAR DATOS DE RIVALES
# ============================================

dashboard_rivales = rivales.copy()

if "porcentaje_exito" in dashboard_rivales.columns:
    dashboard_rivales = dashboard_rivales.sort_values(
        by="porcentaje_exito",
        ascending=False
    )


# ============================================
# 4. PREPARAR DATOS DE ACCIONES
# ============================================

dashboard_acciones = acciones.copy()

if "total_acciones" in dashboard_acciones.columns:
    dashboard_acciones = dashboard_acciones.sort_values(
        by="total_acciones",
        ascending=False
    )


# ============================================
# 5. CREAR INDICADORES GENERALES
# ============================================

total_registros = int(
    dashboard_jugadores["total_eventos"].sum()
)

total_jugadores = int(
    dashboard_jugadores["jugador"].nunique()
)

if "rival" in dashboard_rivales.columns:
    total_rivales = int(
        dashboard_rivales["rival"].nunique()
    )
else:
    total_rivales = len(dashboard_rivales)

promedio_exito = round(
    dashboard_jugadores["porcentaje_exito"].mean(),
    2
)

promedio_rendimiento = round(
    dashboard_jugadores["indice_rendimiento"].mean(),
    2
)

promedio_predicho = round(
    dashboard_jugadores["rendimiento_predicho"].mean(),
    2
)

indicadores = pd.DataFrame({
    "indicador": [
        "Total de registros analizados",
        "Total de jugadores",
        "Total de rivales",
        "Promedio de exito",
        "Promedio de rendimiento",
        "Promedio de rendimiento predicho"
    ],
    "valor": [
        total_registros,
        total_jugadores,
        total_rivales,
        promedio_exito,
        promedio_rendimiento,
        promedio_predicho
    ]
})


# ============================================
# 6. EXPORTAR PARA POWER BI WEB
# ============================================

# IMPORTANTE:
# sep=";"     -> separador entre columnas
# decimal="," -> decimal compatible con español
# utf-8-sig   -> conserva correctamente acentos

dashboard_jugadores.to_csv(
    "powerbi_jugadores.csv",
    index=False,
    sep=";",
    decimal=",",
    encoding="utf-8-sig"
)

dashboard_rivales.to_csv(
    "powerbi_rivales.csv",
    index=False,
    sep=";",
    decimal=",",
    encoding="utf-8-sig"
)

dashboard_acciones.to_csv(
    "powerbi_acciones.csv",
    index=False,
    sep=";",
    decimal=",",
    encoding="utf-8-sig"
)

indicadores.to_csv(
    "powerbi_indicadores.csv",
    index=False,
    sep=";",
    decimal=",",
    encoding="utf-8-sig"
)


# ============================================
# 7. MOSTRAR RESULTADOS
# ============================================

print("\n===== RESUMEN PARA POWER BI =====")

print("\nJugadores:")
print(
    dashboard_jugadores[
        [
            "jugador",
            "posicion",
            "porcentaje_exito",
            "indice_rendimiento",
            "rendimiento_predicho"
        ]
    ].to_string(index=False)
)

print("\nIndicadores generales:")
print(indicadores.to_string(index=False))


print("\n===== ARCHIVOS GENERADOS =====")
print("- powerbi_jugadores.csv")
print("- powerbi_rivales.csv")
print("- powerbi_acciones.csv")
print("- powerbi_indicadores.csv")

print("\nPreparacion para Power BI terminada correctamente.")