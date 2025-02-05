# 创建一个用于设置坐标轴的函数

我们将创建一个函数，用于使用所需的刻度标签来设置坐标轴。

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axislines.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
