# Dreieck unter Cursor hervorheben

Wir möchten das Dreieck unter dem Cursor hervorheben, wenn die Maus über dem Diagramm bewegt wird. Dazu werden wir ein `Polygon`-Objekt erstellen, das mit den Eckpunkten des Dreiecks unter dem Cursor aktualisiert wird. Wir werden `ax.add_patch()` verwenden, um das Polygon zum Diagramm hinzuzufügen.

```python
from matplotlib.patches import Polygon

polygon = Polygon([[0, 0], [0, 0], [0, 0]], facecolor='y')
ax.add_patch(polygon)
```

Wir werden auch eine Funktion `update_polygon()` erstellen, die die Eckpunkte des Polygons mit den Eckpunkten des Dreiecks unter dem Cursor aktualisiert.

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
