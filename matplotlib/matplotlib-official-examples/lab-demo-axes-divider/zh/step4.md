# 绘制时定位的图像与颜色条 - 一种复杂的方法

在这一步中，我们将以一种复杂的方式创建一个图像及其颜色条，并在绘制时进行定位。我们将使用 `mpl_toolkits.axes_grid1` 中的 `SubplotDivider` 为坐标轴和颜色条创建一个分隔器。

```python
def demo_locatable_axes_hard(fig):
    from mpl_toolkits.axes_grid1 import Size, SubplotDivider

    divider = SubplotDivider(fig, 2, 2, 2, aspect=True)

    # 用于图像的坐标轴
    ax = fig.add_subplot(axes_locator=divider.new_locator(nx=0, ny=0))
    # 用于颜色条的坐标轴
    ax_cb = fig.add_subplot(axes_locator=divider.new_locator(nx=2, ny=0))

    divider.set_horizontal([
        Size.AxesX(ax),  # 主坐标轴
        Size.Fixed(0.05),  # 填充，0.1 英寸
        Size.Fixed(0.2),  # 颜色条，0.3 英寸
    ])
    divider.set_vertical([Size.AxesY(ax)])

    Z, extent = get_demo_image()

    im = ax.imshow(Z, extent=extent)
    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.set_tick_params(labelright=False)
```
