# Добавляем стрелку ориентации

Вы можете добавить стрелку ориентации к эллипсу, нанося маркер в конец малой оси. Вы можете использовать метод `get_co_vertices()` для получения координат вершин эллипса. Затем вы можете использовать класс `Affine2D()` для вращения маркера, чтобы он соответствовал углу эллипса.

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
