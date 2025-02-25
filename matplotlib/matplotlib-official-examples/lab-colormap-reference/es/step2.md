# Creando un mapa de colores simple

Para crear un mapa de colores simple, podemos utilizar la clase `ListedColormap` del módulo `matplotlib.colors`. Esta clase toma una lista de colores y crea un mapa de colores a partir de ellos.

```python
import matplotlib.colors as mcolors

# Define una lista de colores
colors = ['red', 'green', 'blue']

# Crea un objeto ListedColormap a partir de la lista de colores
cmap = mcolors.ListedColormap(colors)
```
