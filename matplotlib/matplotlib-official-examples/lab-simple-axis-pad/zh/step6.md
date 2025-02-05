# 调整刻度位置

在这一步中，调整浮动轴上刻度的位置。这可以通过将`major_ticks`对象的`tick_out`属性设置为`True`来实现。

```python
# 调整刻度位置
fig = plt.figure(figsize=(9, 3.))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.01, hspace=0.01)

ax1 = setup_axes(fig, rect=121)
axis = add_floating_axis(ax1)

ax1 = setup_axes(fig, rect=122)
axis = add_floating_axis(ax1)
axis.major_ticks.set_tick_out(True)

plt.show()
```
