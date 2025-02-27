# Introducción

En este laboratorio, aprenderemos cómo aproximar una función con polinomios de un cierto grado utilizando regresión con regularización L2. Mostraremos dos maneras diferentes de hacer esto dados `n_samples` de puntos unidimensionales `x_i`:

1. `PolynomialFeatures`: genera todos los monomios hasta un grado especificado. Esto nos da la matriz de Vandermonde con `n_samples` filas y `degree + 1` columnas.
2. `SplineTransformer`: genera funciones de base B-spline. Una función de base de una B-spline es una función polinómica por tramos de grado `degree` que es no nula solo entre `degree+1` nudos consecutivos.

Usaremos la función `make_pipeline` para agregar características no lineales y mostraremos cómo estos transformadores son adecuados para modelar efectos no lineales con un modelo lineal. Graficaremos la función, los puntos de entrenamiento y la interpolación utilizando características polinómicas y B-splines. También graficaremos todas las columnas de ambos transformadores por separado y mostraremos los nudos de la spline. Finalmente, demostraremos el uso de splines periódicas.

## Consejos sobre la VM

Después de que se complete la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Notebook** para acceder a Jupyter Notebook y practicar.

A veces, es posible que tenga que esperar unos segundos para que Jupyter Notebook termine de cargar. La validación de operaciones no puede automatizarse debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos rápidamente para usted.
