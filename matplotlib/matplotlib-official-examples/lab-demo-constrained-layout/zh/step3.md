# 创建无约束布局的子图

我们创建一个2x2子图的图形，不使用“约束布局”。这会导致轴上的标签重叠。

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout=None)

for ax in axs.flat:
    example_plot(ax)
```
