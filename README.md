
# Barcelona Big Data

### Análisis y predicción del rendimiento de jugadores del FC Barcelona | Temporada 2026/2027

**Proyecto Integrador – Fase 3**

**Universidad:** Tecmilenio, Campus Guadalupe  
**Carrera:** Ingeniería en Desarrollo de Software  
**Alumno:** Abdiel Abraham Hernández Rodríguez  
**Matrícula:** 3067821  
**Docente:** Jonathan Alexis Puente Guerrero  
**Fecha:** 31 de octubre de 2026

---

## Descripción del proyecto

Desarrollé un prototipo de análisis deportivo utilizando herramientas de Big Data para procesar información relacionada con el rendimiento de jugadores del FC Barcelona.

Trabajé con un conjunto de 1,000,000 de registros sintéticos correspondientes a la temporada 2026/2027. Esto me permitió implementar un proceso de generación, limpieza, transformación, procesamiento, almacenamiento, análisis y visualización de datos.

El proyecto integra Python, Apache Spark, MongoDB y Power BI. También desarrollé un modelo experimental para estimar indicadores de rendimiento a partir de los datos preparados.

## Objetivo

Desarrollar una solución que permita procesar grandes volúmenes de datos deportivos, calcular indicadores de rendimiento por jugador, identificar patrones en las acciones registradas y presentar los resultados mediante un dashboard interactivo.

## Tecnologías utilizadas

| Herramienta | Aplicación |
|---|---|
| Python | Generación, limpieza, análisis y predicción |
| pandas y NumPy | Transformación y preparación de datos |
| Apache Spark (PySpark) | Procesamiento y agregación de un millón de registros |
| MongoDB | Almacenamiento de eventos y predicciones |
| MongoDB Compass | Consulta y revisión de la base de datos |
| Power BI | Visualización de indicadores y resultados |
| Visual Studio Code | Desarrollo y ejecución de scripts |
| GitHub | Organización y publicación del código |

## Metodología de desarrollo

Utilicé las etapas de CRISP-DM para organizar el proyecto:

1. **Comprensión del negocio:** definí la necesidad de analizar el rendimiento de jugadores mediante indicadores deportivos.
2. **Comprensión de los datos:** identifiqué las variables necesarias para representar eventos futbolísticos.
3. **Preparación de los datos:** generé, limpié y transformé el conjunto de registros.
4. **Modelado:** desarrollé un modelo experimental para estimar indicadores de rendimiento.
5. **Evaluación:** revisé los resultados del procesamiento y las comparaciones visuales.
6. **Despliegue:** organicé los resultados para su consulta mediante MongoDB y Power BI.

## Implementación del proyecto

### Generación de datos

Utilicé `generar_dataset.py` para crear un conjunto de 1,000,000 de registros sintéticos de eventos futbolísticos.

Los registros incluyen información como jugador, posición, rival, minuto, tipo de acción y resultado.

### Limpieza y transformación

Mediante `limpiar_datos.py` preparé los registros para su procesamiento y análisis.

### Procesamiento con Apache Spark

Ejecuté `procesar_spark.py` para procesar los registros mediante PySpark.

El programa permitió agrupar la información por jugador, tipo de acción y rival, además de calcular indicadores de rendimiento.

La ejecución procesó correctamente 1,000,000 de registros y generó archivos CSV con los resultados agregados.

### Almacenamiento en MongoDB

Utilicé `cargar_mongodb.py` para almacenar los eventos en la base de datos `barcelona_bigdata`.

La colección `eventos` contiene 1,000,000 de documentos.

También incorporé una colección de predicciones para almacenar los resultados del modelo experimental.

### Análisis de datos

Con `analizar_datos.py` realicé consultas y análisis sobre los datos preparados.

### Modelo predictivo

Desarrollé `modelo_prediccion.py` para generar estimaciones experimentales de rendimiento por jugador.

El modelo forma parte del prototipo y requiere validación adicional con datos deportivos reales antes de utilizarse en decisiones profesionales.

### Visualización en Power BI

Preparé archivos CSV para construir un dashboard de tres páginas:

1. Rendimiento actual frente al rendimiento predicho por jugador.
2. Porcentaje de éxito por jugador.
3. Comparación de acciones ofensivas: tiros, goles y asistencias.

## Resultados obtenidos

### Procesamiento general

| Indicador | Resultado |
|---|---|
| Registros generados | 1,000,000 |
| Registros procesados con Spark | 1,000,000 |
| Jugadores analizados | 10 |
| Tipos de acciones | 7 |
| Rivales incluidos | 6 |
| Documentos en MongoDB, colección eventos | 1,000,000 |
| Páginas del dashboard | 3 |

### Rendimiento por jugador

Los siguientes indicadores fueron calculados mediante Apache Spark.

| Jugador | Total de eventos | Acciones exitosas | Porcentaje de éxito |
|---|---:|---:|---:|
| Rodri | 99,529 | 49,968 | 50.20% |
| Anthony Gordon | 99,727 | 49,983 | 50.12% |
| Raphinha | 100,131 | 50,119 | 50.05% |
| Lamine Yamal | 100,228 | 50,150 | 50.04% |
| Gavi | 100,281 | 50,136 | 50.00% |
| Frenkie de Jong | 100,273 | 50,097 | 49.96% |
| Gabriel Jesus | 99,892 | 49,867 | 49.92% |
| Karim Adeyemi | 100,073 | 49,938 | 49.90% |
| Dani Olmo | 99,790 | 49,769 | 49.87% |
| Pedri | 100,076 | 49,830 | 49.79% |

### Acciones registradas

| Acción | Total |
|---|---:|
| Gol | 143,375 |
| Tiro | 143,306 |
| Pase | 143,211 |
| Pérdida | 142,997 |
| Recuperación | 142,607 |
| Regate | 142,514 |
| Asistencia | 141,990 |

Los resultados corresponden a datos simulados y permiten comprobar el funcionamiento del proceso de análisis y agregación.

## Archivos del proyecto

| Archivo | Función |
|---|---|
| `generar_dataset.py` | Generación de registros sintéticos |
| `limpiar_datos.py` | Limpieza y transformación |
| `procesar_spark.py` | Procesamiento con Apache Spark |
| `cargar_mongodb.py` | Almacenamiento de eventos en MongoDB |
| `analizar_datos.py` | Análisis de información |
| `modelo_prediccion.py` | Generación de estimaciones |
| `cargar_predicciones_mongodb.py` | Almacenamiento de predicciones |
| `preparar_powerbi.py` | Preparación de datos para Power BI |
| `powerbi_jugadores.csv` | Datos de rendimiento por jugador |
| `powerbi_acciones.csv` | Datos de acciones deportivas |
| `powerbi_indicadores.csv` | Indicadores para visualización |
| `powerbi_rivales.csv` | Resultados por rival |

## Ejecución del proyecto

Para ejecutar los scripts utilizo Python desde la terminal de Visual Studio Code.

### Instalación de librerías

```bash
python3 -m pip install pandas numpy pyspark pymongo scikit-learn
```

### Ejecución de scripts

```bash
python3 generar_dataset.py
python3 limpiar_datos.py
python3 procesar_spark.py
python3 cargar_mongodb.py
python3 analizar_datos.py
python3 modelo_prediccion.py
python3 cargar_predicciones_mongodb.py
python3 preparar_powerbi.py
```

Las rutas de entrada y salida, así como la conexión a MongoDB, deben configurarse de acuerdo con el entorno de ejecución.

## Aplicación y propuesta de valor

Mi propuesta es adaptar este prototipo como una herramienta de analítica deportiva que permita a clubes, academias y entrenadores organizar información sobre el rendimiento de sus jugadores.

### Clientes potenciales

- Academias y escuelas de fútbol.
- Equipos amateur y semiprofesionales.
- Entrenadores y preparadores físicos.
- Analistas deportivos independientes.
- Clubes que necesiten centralizar información de rendimiento.

### Beneficios

- Centralización de datos deportivos.
- Consulta rápida de indicadores por jugador y partido.
- Comparación de acciones y tendencias de rendimiento.
- Reducción del trabajo manual al elaborar reportes.
- Apoyo a la toma de decisiones deportivas con información organizada.

### Forma de comercialización

Ofrecería una demostración del sistema y posteriormente un proyecto piloto con datos proporcionados y autorizados por el cliente.

El servicio podría ofrecerse mediante:

- Implementación personalizada.
- Suscripción mensual para consulta de indicadores.
- Desarrollo de dashboards específicos.
- Servicio de análisis y generación de reportes.

El precio dependería del número de usuarios, volumen de datos, funcionalidades y necesidades de cada organización.

### Ventaja del proyecto

La solución integra generación, procesamiento, almacenamiento, análisis y visualización de información en un mismo flujo de trabajo.

Además, su estructura puede adaptarse para analizar información de otros equipos y categorías deportivas.

### Mejoras futuras

Para llevar el proyecto a un entorno comercial sería necesario:

- Integrar datos deportivos reales y autorizados.
- Validar el modelo predictivo con métricas de desempeño.
- Incorporar filtros por temporada, partido y posición.
- Implementar usuarios y permisos de acceso.
- Automatizar la actualización de los indicadores.
- Desarrollar una interfaz para clientes.

## Alcance del proyecto

El conjunto de datos utilizado es sintético y de uso académico. No representa estadísticas oficiales del FC Barcelona.

El modelo predictivo es experimental y todavía no se ha validado para su uso en decisiones deportivas profesionales.

## Conclusión

Con este proyecto implementé un proceso de Big Data que abarca desde la generación de un millón de registros hasta su procesamiento con Apache Spark, almacenamiento en MongoDB y visualización en Power BI.

El desarrollo me permitió aplicar herramientas de ingeniería de datos, análisis y programación para construir un prototipo funcional.

También identifiqué la posibilidad de convertirlo en una herramienta de analítica deportiva para academias, entrenadores y clubes, mediante futuras mejoras y el uso de información real.
