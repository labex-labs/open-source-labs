# Crear una norma continua

Crearemos una norma continua para mapear de puntos de datos a colores. Usaremos la función `Normalize` de `matplotlib.pyplot` para normalizar los valores de `dydx` entre su mínimo y máximo. Luego, usaremos la función `LineCollection` para crear un conjunto de segmentos de línea y colorearlos individualmente según su derivada. Usaremos la función `set_array` para establecer los valores utilizados para la asignación de colores.

```python
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
