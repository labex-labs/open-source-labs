# Mettre en évidence le triangle sous le curseur

Nous souhaitons mettre en évidence le triangle sous le curseur lorsque la souris est déplacée sur la représentation graphique. Pour ce faire, nous allons créer un objet `Polygon` qui sera mis à jour avec les sommets du triangle sous le curseur. Nous utiliserons `ax.add_patch()` pour ajouter le polygone à la représentation graphique.

```python
from matplotlib.patches import Polygon

polygon = Polygon([[0, 0], [0, 0], [0, 0]], facecolor='y')
ax.add_patch(polygon)
```

Nous créerons également une fonction `update_polygon()` qui mettra à jour les sommets du polygone avec les sommets du triangle sous le curseur.

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
