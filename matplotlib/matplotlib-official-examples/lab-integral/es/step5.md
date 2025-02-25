# Crear la región sombreada

Crea la región sombreada utilizando un parche `Polygon`. Genera valores de x e y para la región utilizando `linspace` y la función definida en el paso 1. Luego, define los vértices de la región como una lista de tuplas. Finalmente, crea el objeto `Polygon` y agréguelo al eje utilizando `add_patch`.

```python
from matplotlib.patches import Polygon

ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)
```
