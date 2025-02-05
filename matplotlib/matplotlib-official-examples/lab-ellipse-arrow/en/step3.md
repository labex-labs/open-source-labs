# Add an Orientation Arrow

You can add an orientation arrow to the ellipse by plotting a marker at the end point of the minor axis. You can use the `get_co_vertices()` method to get the coordinates of the vertices of the ellipse. Then, you can use the `Affine2D()` class to rotate the marker to match the angle of the ellipse.

```python
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

# Plot an arrow marker at the end point of minor axis
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
