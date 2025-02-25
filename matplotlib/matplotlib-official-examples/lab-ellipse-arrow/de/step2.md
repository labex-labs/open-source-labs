# Ellipse erstellen

Als nächstes musst du eine Ellipse mithilfe der Klasse `Ellipse` erstellen. Du kannst den Mittelpunkt der Ellipse, die Breite und Höhe der Ellipse sowie den Rotationswinkel angeben.

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
