# 创建具有约束布局的子图

我们创建相同的2x2子图，但这次我们使用“约束布局”。这会自动调整子图，以防止轴对象和标签之间出现重叠。

```python
fig, axs = plt.subplots(nrows=2, ncols=2, layout='constrained')

for ax in axs.flat:
    example_plot(ax)
```
