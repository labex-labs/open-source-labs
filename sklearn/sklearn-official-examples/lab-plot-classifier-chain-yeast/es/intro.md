# Introducción

Esta práctica demuestra un ejemplo de uso de la cadena de clasificadores en un conjunto de datos de etiquetado múltiple. El algoritmo de Cadena de Clasificadores es una modificación del método de transformación de problema para la clasificación de etiquetado múltiple. Este método aprovecha la correlación entre las clases mediante la construcción de una cadena de clasificadores binarios. Cada modelo recibe las predicciones de los modelos anteriores en la cadena como características. Usaremos el conjunto de datos `yeast` que contiene 2417 puntos de datos, cada uno con 103 características y 14 etiquetas posibles. Cada punto de datos tiene al menos una etiqueta. Como línea base, primero entrenamos un clasificador de regresión logística para cada una de las 14 etiquetas. Para evaluar el rendimiento de estos clasificadores, hacemos predicciones en un conjunto de prueba separado y calculamos la puntuación de Jaccard para cada muestra.

## Consejos sobre la VM

Una vez que se haya iniciado la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos inmediatamente.
