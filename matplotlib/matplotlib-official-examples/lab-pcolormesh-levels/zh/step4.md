# 使用规范设置级别

展示了如何将归一化（Normalization）和颜色映射（Colormap）实例相结合，以便在`.axes.Axes.pcolor`、`.axes.Axes.pcolormesh`和`.axes.Axes.imshow`类型的图表中绘制“级别”，其方式类似于`contour/contourf`的`levels`关键字参数。

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

# 将这些值设置得更小以提高分辨率
dx, dy = 0.05, 0.05

# 为 x 和 y 边界生成 2 个二维网格
y, x = np.mgrid[slice(1, 5 + dy, dy),
                slice(1, 5 + dx, dx)]

z = np.sin(x)**10 + np.cos(10 + y*x) * np.cos(x)

# x 和 y 是边界，因此 z 应该是这些边界内的值。
# 因此，从 z 数组中删除最后一个值。
z = z[:-1, :-1]
levels = MaxNLocator(nbins=15).tick_values(z.min(), z.max())


# 选择所需的颜色映射，合理设置级别，并定义一个归一化实例，
# 该实例将数据值转换为级别。
cmap = plt.colormaps['PiYG']
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

fig, (ax0, ax1) = plt.subplots(nrows=2)

im = ax0.pcolormesh(x, y, z, cmap=cmap, norm=norm)
fig.colorbar(im, ax=ax0)
ax0.set_title('pcolormesh with levels')


# 等高线是基于点的图表，因此将我们的边界转换为点中心
cf = ax1.contourf(x[:-1, :-1] + dx/2.,
                  y[:-1, :-1] + dy/2., z, levels=levels,
                  cmap=cmap)
fig.colorbar(cf, ax=ax1)
ax1.set_title('contourf with levels')

# 调整子图之间的间距，使 `ax1` 的标题和 `ax0` 的刻度标签不重叠
fig.tight_layout()

plt.show()
```
