# Calcular la información mutua

Ahora calcularemos la puntuación de la información mutua para cada característica. La información mutua puede capturar cualquier tipo de dependencia entre variables. Normalizaremos las puntuaciones de la información mutua dividiéndolas por la puntuación máxima de la información mutua.

```python
mi = mutual_info_regression(X, y)
mi /= np.max(mi)
```
