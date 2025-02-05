# 定义一个用于设置坐标轴的函数

为了简化代码，我们可以定义一个函数，该函数以图形对象和位置作为输入，并返回一个带有自定义刻度标签的坐标轴对象。

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)
    ax.set_yticks([0.2, 0.8], labels=["short", "loooong"])
    ax.set_xticks([0.2, 0.8], labels=[r"$\frac{1}{2}\pi$", r"$\pi$"])
    return ax
```
