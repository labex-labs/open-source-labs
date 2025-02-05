# 设置坐标轴函数

创建一个用于设置坐标轴的函数。此函数将设置x轴和y轴的刻度值。

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
