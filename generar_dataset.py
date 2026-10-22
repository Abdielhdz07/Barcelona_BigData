import pandas as pd
import numpy as np

# Cantidad de registros para el proyecto
cantidad_registros = 1000000

# Jugadores del FC Barcelona 2026/2027
# Cada jugador tiene asignada su posicion
jugadores = {
    "Lamine Yamal": "Delantero",
    "Raphinha": "Delantero",
    "Gabriel Jesus": "Delantero",
    "Karim Adeyemi": "Delantero",
    "Anthony Gordon": "Delantero",
    "Pedri": "Mediocampista",
    "Rodri": "Mediocampista",
    "Gavi": "Mediocampista",
    "Dani Olmo": "Mediocampista",
    "Frenkie de Jong": "Mediocampista"
}

# Rivales
rivales = [
    "Real Madrid",
    "Atletico de Madrid",
    "Sevilla",
    "Valencia",
    "Villarreal",
    "Real Sociedad"
]

# Tipos de acciones
acciones = [
    "Pase",
    "Tiro",
    "Regate",
    "Recuperacion",
    "Perdida",
    "Asistencia",
    "Gol"
]

# Seleccionar jugadores aleatoriamente
jugadores_seleccionados = np.random.choice(
    list(jugadores.keys()),
    cantidad_registros
)

# Crear los datos
datos = {
    "evento_id": range(1, cantidad_registros + 1),

    "temporada": ["2026/2027"] * cantidad_registros,

    "origen_dato": ["sintetico"] * cantidad_registros,

    "partido_id": np.random.randint(
        1,
        39,
        cantidad_registros
    ),

    "jugador": jugadores_seleccionados,

    "posicion": [
        jugadores[jugador]
        for jugador in jugadores_seleccionados
    ],

    "rival": np.random.choice(
        rivales,
        cantidad_registros
    ),

    "minuto": np.random.randint(
        1,
        91,
        cantidad_registros
    ),

    "accion": np.random.choice(
        acciones,
        cantidad_registros
    ),

    "resultado": np.random.choice(
        ["Exitoso", "Fallido"],
        cantidad_registros
    )
}

# Convertir los datos en un DataFrame
df = pd.DataFrame(datos)

# Guardar el dataset en un archivo CSV
df.to_csv(
    "dataset_barcelona.csv",
    index=False
)

# Mostrar los primeros 10 registros
print(df.head(10))

# Mostrar la cantidad total de registros
print("\nTotal de registros:", len(df))

# Confirmar que el archivo fue guardado
print("Dataset guardado correctamente como dataset_barcelona.csv")