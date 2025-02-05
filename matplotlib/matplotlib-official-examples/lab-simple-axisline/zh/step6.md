# 创建第二个y轴

最后，我们将在图表右侧创建一个新的y2轴，其偏移量为(20, 0)并为其添加标签。

```python
ax.axis["right2"] = ax.new_fixed_axis(loc="right", offset=(20, 0))
ax.axis["right2"].label.set_text("Label Y2")
```
