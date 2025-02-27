# Introducción

Esta práctica demuestra cómo utilizar la regresión cuantílica para crear intervalos de predicción con scikit-learn. Generaremos datos sintéticos para un problema de regresión, aplicaremos la función a estos datos y crearemos observaciones de la variable objetivo utilizando una distribución lognormal. Luego, dividiremos los datos en conjuntos de entrenamiento y prueba, ajustaremos regresores cuantílicos no lineales y de mínimos cuadrados y crearemos un conjunto de evaluación de valores de entrada equiespaciados que cubra el rango [0, 10]. Compararemos la mediana predicha con la media predicha, analizaremos las métricas de error y calibraremos el intervalo de confianza. Finalmente, ajustaremos los hiperparámetros de los regresores cuantílicos.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje su retroalimentación después de la sesión y resolveremos el problema inmediatamente para usted.
