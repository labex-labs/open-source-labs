# Ajouter une flèche d'orientation

Vous pouvez ajouter une flèche d'orientation à l'ellipse en traçant un marqueur au point terminal de l'axe mineur. Vous pouvez utiliser la méthode `get_co_vertices()` pour obtenir les coordonnées des sommets de l'ellipse. Ensuite, vous pouvez utiliser la classe `Affine2D()` pour faire tourner le marqueur pour qu'il corresponde à l'angle de l'ellipse.

```python
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

# Trace un marqueur flèche au point terminal de l'axe mineur
vertices = ellipse.get_co_vertices()
t = Affine2D().rotate_deg(ellipse.angle)
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle(">", "full", t),
    markersize=10
)
```
