# Creando mapas de colores personalizados

Matplotlib también permite crear mapas de colores personalizados. Esto puede ser útil cuando los mapas de colores integrados no proporcionan la representación deseada de los datos.

```python
import matplotlib.colors as mcolors

# Define una lista de colores y sus valores correspondientes
colors = [(0,'red'), (0.5, 'green'), (1, 'blue')]

# Crea un objeto LinearSegmentedColormap a partir de la lista de colores
cmap = mcolors.LinearSegmentedColormap.from_list('my_cmap', colors)
```
