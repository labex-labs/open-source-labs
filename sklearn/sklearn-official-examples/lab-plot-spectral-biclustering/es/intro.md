# Introducción

En este laboratorio, usaremos el algoritmo de biclustering espectral para agrupar datos considerando simultáneamente las filas (muestras) y columnas (características) de una matriz. Su objetivo es identificar patrones no solo entre las muestras sino también dentro de subconjuntos de muestras, lo que permite la detección de estructura localizada dentro de los datos. Esto hace que el biclustering espectral sea particularmente adecuado para conjuntos de datos donde el orden o la disposición de las características es fija, como en imágenes, series temporales o genomas. Usaremos la biblioteca scikit-learn para generar un conjunto de datos de tablero de ajedrez y aplicar el algoritmo de biclustering espectral para agruparlo.

## Consejos sobre la VM

Una vez que se haya iniciado la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos rápidamente para usted.
