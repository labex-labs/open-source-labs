# Подсветка треугольника под указателем мыши

Мы хотим подсвечивать треугольник под указателем мыши при перемещении указателя по графику. Для этого мы создадим объект `Polygon`, который будет обновляться вершинами треугольника под указателем мыши. Мы будем использовать `ax.add_patch()`, чтобы добавить многоугольник на график.

```python
from matplotlib.patches import Polygon

polygon = Polygon([[0, 0], [0, 0], [0, 0]], facecolor='y')
ax.add_patch(polygon)
```

Мы также создадим функцию `update_polygon()`, которая будет обновлять вершины многоугольника вершинами треугольника под указателем мыши.

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
