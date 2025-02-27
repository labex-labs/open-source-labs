# Introducción

Esta práctica demuestra un problema de clasificación de documentos con múltiples etiquetas utilizando scikit-learn. El conjunto de datos se genera aleatoriamente según el siguiente proceso:

- Elegir el número de etiquetas: n ~ Poisson(n_labels)
- N veces, elegir una clase c: c ~ Multinomial(theta)
- Elegir la longitud del documento: k ~ Poisson(length)
- K veces, elegir una palabra: w ~ Multinomial(theta_c)

En este proceso, se utiliza muestreo de rechazo para garantizar que n sea mayor que 2 y que la longitud del documento nunca sea cero. Del mismo modo, se rechazan las clases que ya han sido elegidas. Los documentos que se asignan a ambas clases se representan rodeados de dos círculos de colores diferentes.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos rápidamente para usted.
