# Media Ponderada

Escribe una función `weighted_average(nums, weights)` que tome dos listas de la misma longitud: `nums` y `weights`. La función debe devolver la media ponderada de los números en `nums`, donde cada número se multiplica por su peso correspondiente en `weights`. La media ponderada se calcula dividiendo la suma de los productos de cada número y su peso por la suma de los pesos.

```python
def weighted_average(nums, weights):
  return sum(x * y for x, y in zip(nums, weights)) / sum(weights)
```

```python
weighted_average([1, 2, 3], [0.6, 0.2, 0.3]) # 1.72727
```
