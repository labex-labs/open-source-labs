# Introducción

En este laboratorio, exploraremos cómo la complejidad del modelo influye en la precisión de predicción y el rendimiento computacional. Utilizaremos dos conjuntos de datos: el Conjunto de Datos de Diabetes para regresión y el Conjunto de Datos 20newsgroups para clasificación. Modelaremos la influencia de la complejidad en tres estimadores diferentes:

- SGDClassifier (para datos de clasificación) que implementa el aprendizaje por descenso de gradiente estocástico
- NuSVR (para datos de regresión) que implementa la regresión de vectores de soporte Nu
- GradientBoostingRegressor que construye un modelo aditivo de manera secuencial en etapas

Variaremos la complejidad del modelo a través de la selección de parámetros de modelo relevantes en cada uno de nuestros modelos seleccionados. A continuación, mediremos la influencia en el rendimiento computacional (latencia) y la capacidad predictiva (MSE o Pérdida de Hamming).

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de operaciones no puede automatizarse debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje su retroalimentación después de la sesión y resolveremos rápidamente el problema para usted.
