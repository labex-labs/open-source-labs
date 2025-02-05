# 突出显示光标下方的三角形

当鼠标在绘图区域移动时，我们希望突出显示光标下方的三角形。为此，我们将创建一个 `Polygon` 对象，该对象将使用光标下方三角形的顶点进行更新。我们将使用 `ax.add_patch()` 将多边形添加到绘图中。

```python
from matplotlib.patches import Polygon

polygon = Polygon([[0, 0], [0, 0], [0, 0]], facecolor='y')
ax.add_patch(polygon)
```

我们还将创建一个函数 `update_polygon()`，该函数将使用光标下方三角形的顶点更新多边形的顶点。

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
