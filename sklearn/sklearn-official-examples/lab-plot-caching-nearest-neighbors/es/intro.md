# Introducción

Esta práctica demuestra cómo precomputar los k vecinos más cercanos antes de utilizarlos en KNeighborsClassifier. KNeighborsClassifier puede calcular internamente los vecinos más cercanos, pero precomputarlos puede tener varios beneficios, como un control más fino de los parámetros, el almacenamiento en caché para su uso múltiple o implementaciones personalizadas. Aquí utilizamos la propiedad de almacenamiento en caché de las tuberías para almacenar en caché el gráfico de vecinos más cercanos entre múltiples ajustes de KNeighborsClassifier.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos rápidamente para usted.
