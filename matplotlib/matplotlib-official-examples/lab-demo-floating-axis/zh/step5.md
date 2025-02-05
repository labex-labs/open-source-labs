# 创建浮动坐标轴

在这一步中，我们将创建两个浮动坐标轴，用于在矩形框中显示极坐标曲线。我们将使用 `new_floating_axis()` 来创建浮动坐标轴。

```python
# 创建浮动坐标轴
ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 60)
axis.label.set_text(r"$\theta = 60^{\circ}$")
axis.label.set_visible(True)

ax1.axis["lon"] = axis = ax1.new_floating_axis(1, 6)
axis.label.set_text(r"$r = 6$")
```
