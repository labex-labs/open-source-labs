# Highlight Triangle Under Cursor

We want to highlight the triangle under the cursor as the mouse is moved over the plot. To do this, we will create a `Polygon` object that will be updated with the vertices of the triangle under the cursor. We will use `ax.add_patch()` to add the polygon to the plot.

```python
from matplotlib.patches import Polygon

polygon = Polygon([[0, 0], [0, 0], [0, 0]], facecolor='y')
ax.add_patch(polygon)
```

We will also create a function `update_polygon()` that will update the vertices of the polygon with the vertices of the triangle under the cursor.

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
