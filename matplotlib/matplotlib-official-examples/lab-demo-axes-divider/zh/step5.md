# 绘制时定位的图像与颜色条 - 一种简单的方法

在这一步中，我们将以一种简单的方式创建一个图像及其颜色条，并在绘制时进行定位。我们将使用 `mpl_toolkits.axes_grid1` 中的 `make_axes_locatable` 为坐标轴和颜色条创建一个分隔器。

```python
def demo_locatable_axes_easy(ax):
    from mpl_toolkits.axes_grid1 import make_axes_locatable

    divider = make_axes_locatable(ax)

    ax_cb = divider.append_axes("right", size="5%", pad=0.05)
    fig = ax.get_figure()
    fig.add_axes(ax_cb)

    Z, extent = get_demo_image()
    im = ax.imshow(Z, extent=extent)

    plt.colorbar(im, cax=ax_cb)
    ax_cb.yaxis.tick_right()
    ax_cb.yaxis.set_tick_params(labelright=False)
```
