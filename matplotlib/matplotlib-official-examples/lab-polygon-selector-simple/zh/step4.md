# 综合运用

让我们创建一个完整的示例，其中包括以编程方式和交互式方式创建多边形。

```python
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector

# 创建一个图形和坐标轴
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

# 创建一个多边形选择器对象并添加顶点
selector1 = PolygonSelector(ax1, lambda *args: None)
selector1.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# 绘制多边形
ax1.add_patch(plt.Polygon(selector1.verts, alpha=0.3))

# 创建另一个用于交互式创建的多边形选择器对象
selector2 = PolygonSelector(ax2, lambda *args: None)

print("点击图形以创建多边形。")
print("按 'esc' 键开始绘制新的多边形。")
print("尝试按住'shift' 键以移动所有顶点。")
print("尝试按住 'ctrl' 键以移动单个顶点。")

plt.show()
```
