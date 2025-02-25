# Créer une ellipse

Ensuite, vous devez créer une ellipse à l'aide de la classe `Ellipse`. Vous pouvez spécifier le centre de l'ellipse, la largeur et la hauteur de l'ellipse, et l'angle de rotation.

```python
from matplotlib.patches import Ellipse

ellipse = Ellipse(
    xy=(2, 4),
    width=30,
    height=20,
    angle=35,
    facecolor="none",
    edgecolor="b"
)
ax.add_patch(ellipse)
```
