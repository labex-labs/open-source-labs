# Resumen

Esta práctica demostró cómo precomputar la matriz de Gram mientras se utilizan muestras ponderadas con un ElasticNet. Primero cargamos un conjunto de datos de regresión y creamos un vector de pesos lognormal que se normalizó para sumar el número total de muestras. Luego centramos la matriz de diseño, la reescalamos con los pesos normalizados y calculamos la matriz de Gram. Finalmente, ajustamos la red elástica utilizando la matriz de Gram precomputada y los pesos normalizados.
