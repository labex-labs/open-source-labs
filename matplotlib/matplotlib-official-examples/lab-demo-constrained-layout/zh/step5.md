# 使用约束布局创建嵌套网格布局

我们通过使用带有“约束布局”的嵌套网格布局来创建一个更复杂的示例。这使我们能够对子图的布局有更多的控制权。

```python
fig = plt.figure(layout='constrained')

gs0 = gridspec.GridSpec(1, 2, figure=fig)

gs1 = gridspec.GridSpecFromSubplotSpec(3, 1, subplot_spec=gs0[0])
for n in range(3):
    ax = fig.add_subplot(gs1[n])
    example_plot(ax)


gs2 = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs0[1])
for n in range(2):
    ax = fig.add_subplot(gs2[n])
    example_plot(ax)

plt.show()
```
