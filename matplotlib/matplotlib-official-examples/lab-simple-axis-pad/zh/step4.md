# 为刻度标签添加填充

在这一步中，为浮动轴上的刻度标签添加填充。这可以通过将`major_ticklabels`对象的`pad`属性设置为所需的填充值来实现。

```python
# 为刻度标签添加填充
fig = plt.figure(figsize=(9, 3.))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.01, top=0.99, wspace=0.01, hspace=0.01)

ax1 = setup_axes(fig, rect=121)
axis = add_floating_axis(ax1)

ax1 = setup_axes(fig, rect=122)
axis = add_floating_axis(ax1)
axis.major_ticklabels.set_pad(10)

plt.show()
```
