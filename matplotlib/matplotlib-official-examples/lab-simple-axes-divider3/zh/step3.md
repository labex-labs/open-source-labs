# 设置坐标轴分隔器

我们将使用 `mpl_toolkits.axes_grid1.axes_size` 模块中的 `Divider` 类以及 `AxesX` 和 `AxesY` 类来设置坐标轴分隔器。然后，我们将使用 `new_locator` 方法来设置每个坐标轴的位置。

```python
horiz = [Size.AxesX(ax[0]), Size.Fixed(.5), Size.AxesX(ax[1])]
vert = [Size.AxesY(ax[0]), Size.Fixed(.5), Size.AxesY(ax[2])]
divider = Divider(fig, rect, horiz, vert, aspect=False)

ax[0].set_axes_locator(divider.new_locator(nx=0, ny=0))
ax[1].set_axes_locator(divider.new_locator(nx=2, ny=0))
ax[2].set_axes_locator(divider.new_locator(nx=0, ny=2))
ax[3].set_axes_locator(divider.new_locator(nx=2, ny=2))
```
