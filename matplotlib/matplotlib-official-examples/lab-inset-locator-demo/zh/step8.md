# 在图形坐标中创建居中的内嵌图

通过使用 `blended_transform_factory()` 方法创建一个混合变换，并将其用作 `bbox_transform` 参数，我们可以创建一个在内嵌图在图形坐标中水平居中且垂直方向与坐标轴对齐的内嵌图。

```python
# 创建一个在内嵌图在图形坐标中水平居中且垂直方向
# 与坐标轴对齐的内嵌图。
from matplotlib.transforms import blended_transform_factory

transform = blended_transform_factory(fig.transFigure, ax2.transAxes)
axins4 = inset_axes(ax2, width="16%", height="34%",
                    bbox_to_anchor=(0, 0, 1, 1),
                    bbox_transform=transform, loc=8, borderpad=0)
```
