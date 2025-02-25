# Resaltar el triángulo debajo del cursor

Queremos resaltar el triángulo debajo del cursor a medida que el mouse se mueve sobre la gráfica. Para hacer esto, crearemos un objeto `Polygon` que se actualizará con los vértices del triángulo debajo del cursor. Utilizaremos `ax.add_patch()` para agregar el polígono a la gráfica.

```python
from matplotlib.patches import Polygon

polygon = Polygon([[0, 0], [0, 0], [0, 0]], facecolor='y')
ax.add_patch(polygon)
```

También crearemos una función `update_polygon()` que actualizará los vértices del polígono con los vértices del triángulo debajo del cursor.

```python
def update_polygon(tri):
    if tri == -1:
        points = [0, 0, 0]
    else:
        points = triang.triangles[tri]
    xs = triang.x[points]
    ys = triang.y[points]
    polygon.set_xy(np.column_stack([xs, ys]))
```
