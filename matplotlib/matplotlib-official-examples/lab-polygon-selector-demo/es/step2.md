# Crear datos

En este paso, crearemos algunos datos para visualizar. Crearemos un diagrama de dispersión de puntos en una cuadrícula.

```python
fig, ax = plt.subplots()
grid_size = 5
grid_x = np.tile(np.arange(grid_size), grid_size)
grid_y = np.repeat(np.arange(grid_size), grid_size)
pts = ax.scatter(grid_x, grid_y)
```
