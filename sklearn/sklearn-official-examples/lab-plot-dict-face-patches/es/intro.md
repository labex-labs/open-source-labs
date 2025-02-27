# Introducción

Esta práctica demuestra cómo utilizar la API de scikit-learn para procesar un gran conjunto de datos de caras y aprender un conjunto de parches de imágenes de 20 x 20 que representan caras. El aspecto clave de esta práctica es el uso del aprendizaje en línea, donde cargamos y procesamos imágenes una por una y extraemos 50 parches aleatorios de cada imagen. Acumulamos 500 parches (de 10 imágenes) y luego ejecutamos el método partial_fit del objeto KMeans en línea, MiniBatchKMeans.

## Consejos sobre la VM

Una vez que se haya iniciado la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos rápidamente para usted.
