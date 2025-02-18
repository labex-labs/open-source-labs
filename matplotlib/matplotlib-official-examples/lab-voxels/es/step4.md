# Establecer colores

Ahora estableceremos los colores para cada objeto en el gráfico de voxeles. Lo haremos creando una matriz vacía del mismo tamaño que la matriz booleana que creamos en el Paso 3, y luego estableciendo el color de cada objeto según su ubicación.

```python
colors = np.empty(voxelarray.shape, dtype=object)
colors[link] = 'red'
colors[cube1] = 'blue'
colors[cube2] = 'green'
```
