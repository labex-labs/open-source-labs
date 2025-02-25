# Orientierungsrichtung hinzufügen

Du kannst einer Ellipse eine Orientierungsrichtung hinzufügen, indem du einen Marker am Endpunkt der kleinen Achse zeichnest. Du kannst die Methode `get_co_vertices()` verwenden, um die Koordinaten der Eckpunkte der Ellipse zu erhalten. Anschließend kannst du die Klasse `Affine2D()` verwenden, um den Marker zu drehen, um den Winkel der Ellipse zu entsprechen.

```python
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

# Zeichnen Sie einen Pfeilmarker am Endpunkt der kleinen Achse
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
