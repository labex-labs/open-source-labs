# Crear una elipse

A continuación, debe crear una elipse utilizando la clase `Ellipse`. Puede especificar el centro de la elipse, el ancho y alto de la elipse, y el ángulo de rotación.

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
