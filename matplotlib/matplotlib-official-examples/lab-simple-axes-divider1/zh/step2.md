# 定义辅助函数

我们将定义一个辅助函数 `label_axes()`，用于在坐标轴中心放置一个标签，并移除坐标轴刻度。

```python
def label_axes(ax, text):
    """Place a label at the center of an Axes, and remove the axis ticks."""
    ax.text(.5,.5, text, transform=ax.transAxes,
            horizontalalignment="center", verticalalignment="center")
    ax.tick_params(bottom=False, labelbottom=False,
                   left=False, labelleft=False)
```
