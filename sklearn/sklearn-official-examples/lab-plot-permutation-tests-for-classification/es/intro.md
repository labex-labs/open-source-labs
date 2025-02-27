# Introducción

En el aprendizaje automático, a menudo evaluamos el rendimiento de un modelo de clasificación utilizando una puntuación. Sin embargo, también necesitamos probar la significancia de la puntuación para asegurarnos de que el rendimiento del modelo no sea solo por casualidad. Aquí es donde la prueba de permutación de puntuación resulta útil. Genera una distribución nula calculando la precisión del clasificador en 1000 permutaciones diferentes del conjunto de datos. Luego, se calcula un valor p empírico como el porcentaje de permutaciones para las cuales la puntuación obtenida es mayor que la puntuación obtenida utilizando los datos originales. En este laboratorio, usaremos la función `permutation_test_score` de `sklearn.model_selection` para evaluar la significancia de una puntuación validada cruzada utilizando permutaciones.

## Consejos sobre la VM

Una vez que se haya iniciado la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje comentarios después de la sesión y resolveremos rápidamente el problema para usted.
