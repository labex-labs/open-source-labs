# 添加浮动轴

我们将定义两个函数，用于向绘图中添加浮动轴。第一个函数 `add_floating_axis1()` 向绘图中添加一个标签为 `theta = 30` 的浮动轴。第二个函数 `add_floating_axis2()` 向绘图中添加一个标签为 `r = 6` 的浮动轴。

```python
def add_floating_axis1(ax):
    ax.axis["lat"] = axis = ax.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)
    return axis

def add_floating_axis2(ax):
    ax.axis["lon"] = axis = ax.new_floating_axis(1, 6)
    axis.label.set_text(r"$r = 6$")
    axis.label.set_visible(True)
    return axis
```
