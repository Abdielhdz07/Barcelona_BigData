Barcelona Big Data
Análisis y predicción del rendimiento de jugadores del FC Barcelona | Temporada 2026/2027

Proyecto Integrador – Fase 3
Universidad: Tecmilenio, Campus Guadalupe
Carrera: Ingeniería en Desarrollo de Software
Alumno: Abdiel Abraham Hernández Rodríguez
Matrícula: 3067821
Docente: Jonathan Alexis Puente Guerrero
Fecha: 31/102026

Descripción del proyecto
Desarrollé un prototipo de análisis deportivo utilizando herramientas de Big Data para procesar información relacionada con el rendimiento de jugadores del FC Barcelona. Trabajé con un conjunto de 1,000,000 de registros sintéticos de la temporada 2026/2027, que me permitió implementar un flujo completo de generación, limpieza, procesamiento, almacenamiento, análisis y visualización de datos.

El proyecto integra Python, Apache Spark, MongoDB y Power BI. También desarrollé un modelo experimental para estimar indicadores de rendimiento a partir de los datos preparados.
Objetivo
Desarrollar una solución que permita procesar grandes volúmenes de datos deportivos, calcular indicadores de rendimiento por jugador, identificar patrones en las acciones registradas y presentar los resultados mediante un dashboard interactivo.
Tecnologías utilizadas
Herramienta	Aplicación
Python	Generación, limpieza, análisis y predicción
pandas y NumPy	Transformación y preparación de datos
Apache Spark (PySpark)	Procesamiento y agregación de un millón de registros
MongoDB y MongoDB Compass	Almacenamiento y consulta de eventos y predicciones
Power BI	Visualización de indicadores y resultados
Visual Studio Code	Desarrollo y ejecución de los scripts
GitHub	Organización y publicación del código


Metodología de desarrollo
Utilicé las etapas de CRISP-DM para organizar el proyecto:
1. Comprensión del negocio: definí la necesidad de analizar el rendimiento de jugadores mediante indicadores.
2. Comprensión de los datos: identifiqué las variables necesarias para representar jugadores, partidos, rivales y acciones.
3. Preparación de los datos: generé y limpié un millón de registros sintéticos.
4. Modelado: desarrollé un modelo experimental de predicción de rendimiento.
5. Evaluación: revisé los resultados obtenidos y las diferencias entre jugadores.
6. Presentación de resultados: almacené los datos en MongoDB y construí un dashboard en Power BI.
Desarrollo e implementación
El flujo del proyecto comprende las siguientes actividades:
1. Generación del conjunto de datos con Python.
2. Limpieza y transformación de registros.
3. Procesamiento con Apache Spark y cálculo de indicadores.
4. Almacenamiento de eventos y predicciones en MongoDB.
5. Análisis y generación de estimaciones de rendimiento.
6. Preparación de archivos CSV y visualización en Power BI.
Archivos principales
Archivo	Descripción
generar_dataset.py	Genera el conjunto de datos sintéticos
limpiar_datos.py	Prepara y limpia los registros
procesar_spark.py	Procesa los eventos y calcula indicadores con Spark
cargar_mongodb.py	Almacena los eventos en MongoDB
analizar_datos.py	Analiza los datos preparados
modelo_prediccion.py	Ejecuta el modelo experimental de predicción
cargar_predicciones_mongodb.py	Almacena los resultados de predicción
preparar_powerbi.py	Prepara los archivos para Power BI
powerbi_jugadores.csv	Datos de jugadores para visualización
powerbi_acciones.csv	Datos de acciones para visualización
powerbi_indicadores.csv	Indicadores de rendimiento
powerbi_rivales.csv	Indicadores por rival


Resultados obtenidos
Procesé 1,000,000 de registros mediante Apache Spark y generé una tabla de indicadores para diez jugadores. Los resultados se exportaron a CSV para continuar con el análisis.
Jugador	Eventos	Acciones exitosas	Acciones ofensivas	Éxito (%)
Rodri	99,529	49,968	56,897	50.20
Anthony Gordon	99,727	49,983	57,233	50.12
Raphinha	100,131	50,119	57,240	50.05
Lamine Yamal	100,228	50,150	56,766	50.04
Gavi	100,281	50,136	57,347	50.00
Frenkie de Jong	100,273	50,097	57,188	49.96
Gabriel Jesus	99,892	49,867	57,133	49.92
Karim Adeyemi	100,073	49,938	57,210	49.90
Dani Olmo	99,790	49,769	57,104	49.87
Pedri	100,076	49,830	57,067	49.79


En MongoDB almacené el millón de documentos en la base de datos barcelona_bigdata, colección eventos, y preparé una colección adicional llamada predicciones.
Dashboard de Power BI
El informe contiene tres páginas:
- Rendimiento actual y rendimiento predicho por jugador: comparación de los indicadores generados.
- Porcentaje de éxito por jugador: distribución de las acciones exitosas.
- Acciones ofensivas por jugador: comparación de tiros, goles y asistencias.
Los datos utilizados para construir el informe se encuentran en los archivos powerbi_*.csv del repositorio.
Ejecución del proyecto
Desarrollé el proyecto en macOS con Python 3.12.3 y Visual Studio Code. Para ejecutarlo se requieren las librerías utilizadas en los scripts, un entorno compatible con PySpark y una conexión a MongoDB.
python3 generar_dataset.py
python3 limpiar_datos.py
python3 procesar_spark.py
python3 cargar_mongodb.py
python3 analizar_datos.py
python3 modelo_prediccion.py
python3 cargar_predicciones_mongodb.py
python3 preparar_powerbi.py
Las rutas de entrada y salida y la conexión a MongoDB deben configurarse de acuerdo con el entorno de ejecución.
Aplicación y propuesta de valor
Mi propuesta es adaptar este prototipo como una herramienta de analítica deportiva que permita a clubes, academias y entrenadores organizar datos de sus jugadores y consultar indicadores en un solo lugar.
Clientes potenciales
- Academias y escuelas de fútbol.
- Equipos amateur y semiprofesionales.
- Entrenadores y preparadores físicos.
- Analistas deportivos independientes.
- Clubes que necesiten centralizar información de rendimiento.
Beneficios
- Centralización de datos deportivos.
- Consulta rápida de indicadores por jugador y partido.
- Comparación de acciones y tendencias de rendimiento.
- Reducción del trabajo manual al elaborar reportes.
- Apoyo a la toma de decisiones deportivas con información organizada.
Forma de comercialización
Ofrecería una demostración del sistema y posteriormente un proyecto piloto con datos proporcionados y autorizados por el cliente. El servicio podría incluir configuración, personalización del dashboard, capacitación y mantenimiento, con un costo de implementación y una cuota opcional de soporte.

Para llevarlo a un entorno comercial sería necesario trabajar con datos reales autorizados, validar el modelo predictivo y adaptar los indicadores a las necesidades de cada organización.
Alcance del proyecto
El conjunto de datos utilizado es sintético y de uso académico; no representa estadísticas oficiales del FC Barcelona. El modelo predictivo es experimental y sus resultados no han sido validados con información deportiva real. El proyecto demuestra el funcionamiento del proceso técnico y establece una base para futuras aplicaciones.
Conclusión
Con este proyecto implementé un proceso de Big Data que abarca desde la generación de un millón de registros hasta su procesamiento con Apache Spark, almacenamiento en MongoDB y visualización en Power BI. Además de aplicar las tecnologías estudiadas, identifiqué una oportunidad para adaptar la solución a organizaciones deportivas que necesiten analizar su información de manera más organizada.
