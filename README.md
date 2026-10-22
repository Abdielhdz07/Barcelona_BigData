
# Barcelona Big Data
## Análisis y predicción del rendimiento de jugadores del FC Barcelona

### Proyecto académico - Fase 3
**Universidad:** Tecmilenio  
**Carrera:** Ingeniería en Desarrollo de Software  
**Alumno:** Abdiel Abraham Hernández Rodríguez  
**Matrícula:** 3067821  
**Campus:** Guadalupe  
**Materia:** Proyecto integrador de tecnologías de Big Data
**Docente:** Jonathan Alexis Puente Guerrero  

## 1. Descripción del proyecto

Este proyecto tiene como objetivo analizar y predecir el rendimiento de jugadores del FC Barcelona mediante técnicas de Big Data, utilizando Python, Apache Spark, MongoDB y Power BI.

Se trabaja con un conjunto de datos sintéticos de 1,000,000 de registros que simulan acciones realizadas durante partidos de fútbol. Estos datos permiten estudiar el comportamiento de los jugadores, generar indicadores y desarrollar un modelo de predicción.

Los registros son simulados con fines académicos y no representan estadísticas oficiales del club.

## 2. Objetivo

Desarrollar un proceso de análisis de datos que permita identificar patrones de rendimiento individual y generar estimaciones para apoyar la evaluación de jugadores.

## 3. Tecnologías utilizadas

- Python: generación, limpieza y análisis de datos.
- Pandas y NumPy: manipulación y transformación de información.
- Apache Spark (PySpark): procesamiento de grandes volúmenes de datos.
- MongoDB: almacenamiento de datos y resultados.
- Power BI: visualización de indicadores y comparaciones.
- Visual Studio Code: desarrollo del proyecto.
- GitHub: publicación y control de versiones.

## 4. Archivos del proyecto

| Archivo | Descripción |
|---|---|
| generar_dataset.py | Generación de un millón de registros sintéticos. |
| limpiar_datos.py | Limpieza y preparación del conjunto de datos. |
| procesar_spark.py | Procesamiento de información mediante Apache Spark. |
| cargar_mongodb.py | Carga de datos en MongoDB. |
| analizar_datos.py | Análisis de resultados e indicadores. |
| modelo_prediccion.py | Desarrollo del modelo de predicción. |
| cargar_predicciones_mongodb.py | Almacenamiento de resultados predictivos. |
| preparar_powerbi.py | Preparación de información para visualizaciones. |

## 5. Archivos para Power BI

- powerbi_jugadores.csv
- powerbi_acciones.csv
- powerbi_indicadores.csv
- powerbi_rivales.csv

Estos archivos contienen información preparada para construir gráficos de rendimiento, acciones y comparaciones entre jugadores.

## 6. Metodología CRISP-DM

El proyecto se organiza mediante las siguientes fases:

1. Comprensión del negocio.
2. Comprensión de los datos.
3. Preparación de los datos.
4. Modelado.
5. Evaluación.
6. Despliegue de resultados.

## 7. Proceso general

1. Generar los registros sintéticos.
2. Limpiar y transformar los datos con Python.
3. Procesar la información mediante Apache Spark.
4. Almacenar los resultados en MongoDB.
5. Realizar el análisis de rendimiento.
6. Generar estimaciones mediante el modelo predictivo.
7. Preparar los archivos para Power BI.
8. Visualizar y comparar los resultados.

## 8. Visualización de resultados

El proyecto contempla un informe de Power BI con gráficos sobre:

- Rendimiento actual y rendimiento predicho por jugador.
- Porcentaje de éxito de acciones.
- Comparación de acciones deportivas.
- Indicadores generales de rendimiento.
- Comparación de resultados frente a diferentes rivales.

## 9. Alcance y limitaciones

El análisis se desarrolla como un prototipo académico. Debido a que utiliza datos sintéticos, las predicciones sirven para demostrar el funcionamiento del proceso analítico y no deben interpretarse como pronósticos reales del rendimiento deportivo.

## 10. Conclusión

Este proyecto permite aplicar conocimientos de Ingeniería en Desarrollo de Software y Big Data mediante la integración de diferentes herramientas para generar, procesar, almacenar, analizar y visualizar grandes volúmenes de información.

El resultado es un flujo de trabajo que demuestra cómo los datos pueden utilizarse para apoyar el análisis del rendimiento deportivo.
