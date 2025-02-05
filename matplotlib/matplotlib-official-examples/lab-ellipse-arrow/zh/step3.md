# 添加方向箭头

你可以通过在短轴的端点处绘制一个标记来向椭圆添加方向箭头。你可以使用 `get_co_vertices()` 方法获取椭圆顶点的坐标。然后，你可以使用 `Affine2D()` 类旋转该标记以匹配椭圆的角度。

```python
from matplotlib.markers import MarkerStyle
from matplotlib.transforms import Affine2D

# 在短轴的端点处绘制一个箭头标记
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
