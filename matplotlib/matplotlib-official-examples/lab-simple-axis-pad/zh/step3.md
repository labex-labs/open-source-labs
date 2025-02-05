# 定义添加浮动轴函数

定义`add_floating_axis`函数，该函数用于向图表添加一个浮动轴。此函数将`ax1`对象作为参数传入，并返回`axis`对象。

```python
def add_floating_axis(ax1):
    # 定义浮动轴
    ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)

    return axis
```
