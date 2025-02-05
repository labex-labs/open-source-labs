# 创建内嵌轴

在这一步中，我们使用 `fig.add_axes` 在主绘图轴内创建两个内嵌轴。一个将显示数据的直方图，另一个将显示脉冲响应。

```python
# 创建右侧内嵌轴
right_inset_ax = fig.add_axes([.65,.6,.2,.2], facecolor='k')
right_inset_ax.hist(s, 400, density=True)
right_inset_ax.set(title='Probability', xticks=[], yticks=[])

# 创建左侧内嵌轴
left_inset_ax = fig.add_axes([.2,.6,.2,.2], facecolor='k')
left_inset_ax.plot(t[:len(r)], r)
left_inset_ax.set(title='Impulse response', xlim=(0,.2), xticks=[], yticks=[])
```
