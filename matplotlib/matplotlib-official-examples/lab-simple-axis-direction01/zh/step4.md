# 设置轴标签

我们使用`ax1.axis[]`函数为绘图的左右两侧设置轴标签。我们还使用`set_axis_direction()`函数设置刻度标签的方向。

```python
ax1.axis["left"].major_ticklabels.set_axis_direction("top")
ax1.axis["left"].label.set_text("左标签")

ax1.axis["right"].label.set_visible(True)
ax1.axis["right"].label.set_text("右标签")
ax1.axis["right"].label.set_axis_direction("left")
```
