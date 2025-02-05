# 创建阴影区域

使用 `Polygon` 补丁创建阴影区域。使用 `linspace` 和步骤 1 中定义的函数生成该区域的 x 和 y 值。然后，将该区域的顶点定义为元组列表。最后，创建 `Polygon` 对象并使用 `add_patch` 将其添加到轴上。

```python
from matplotlib.patches import Polygon

ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)
```
