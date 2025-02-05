# 创建一个用于设置坐标轴的函数

我们将创建一个名为 `setup_axes` 的函数来为我们的绘图设置坐标轴。这个函数接受两个参数，一个 `fig` 对象和一个 `pos` 对象。`fig` 对象是我们要在其上绘图的图形对象，而 `pos` 对象是子图在图形中的位置。

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)

    ax.set_ylim(-0.1, 1.5)
    ax.set_yticks([0, 1])

    ax.axis[:].set_visible(False)

    ax.axis["x"] = ax.new_floating_axis(1, 0.5)
    ax.axis["x"].set_axisline_style("->", size=1.5)

    return ax
```
