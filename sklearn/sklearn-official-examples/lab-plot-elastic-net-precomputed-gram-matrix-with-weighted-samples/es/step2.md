# Precomputación de la matriz de Gram con muestras ponderadas

Para ajustar la red elástica utilizando la opción `precompute` junto con los pesos de muestra, primero debemos centrar la matriz de diseño y reescalarla con los pesos normalizados antes de calcular la matriz de Gram. Centramos la matriz de diseño restando el promedio ponderado de cada columna de características de cada fila. Luego, reescalamos la matriz de diseño centrada multiplicando cada fila por la raíz cuadrada del peso normalizado correspondiente. Finalmente, calculamos la matriz de Gram tomando el producto punto de la matriz de diseño reescalada con su traspuesta.

```python
X_offset = np.average(X, axis=0, weights=normalized_weights)
X_centered = X - np.average(X, axis=0, weights=normalized_weights)
X_scaled = X_centered * np.sqrt(normalized_weights)[:, np.newaxis]
gram = np.dot(X_scaled.T, X_scaled)
```
