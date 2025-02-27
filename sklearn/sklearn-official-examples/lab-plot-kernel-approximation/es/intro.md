# Introducción

Esta práctica ilustra la aproximación del mapa de características de un kernel RBF utilizando RBFSampler y Nystroem para aproximar el mapa de características de un kernel RBF para la clasificación con un SVM en el conjunto de datos de dígitos. Se comparan los resultados utilizando un SVM lineal en el espacio original, un SVM lineal utilizando las aproximaciones de mapeo y un SVM con kernel. Se muestran los tiempos y la precisión para diferentes cantidades de muestreos de Monte Carlo (en el caso de RBFSampler, que utiliza características de Fourier aleatorias) y diferentes subconjuntos de tamaño del conjunto de entrenamiento (para Nystroem) para el mapeo aproximado.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje su retroalimentación después de la sesión y resolveremos rápidamente el problema para usted.
