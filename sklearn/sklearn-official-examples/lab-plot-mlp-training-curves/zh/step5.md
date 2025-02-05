# 绘制每个数据集的学习曲线

最后，我们可以使用plot_on_dataset函数为每个数据集绘制学习曲线。我们将创建一个2x2的图，并在单独的轴上绘制每个数据集。

```python
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

for ax, data, name in zip(
    axes.ravel(), data_sets, ["鸢尾花", "手写数字", "圆圈", "月亮"]
):
    plot_on_dataset(*data, ax=ax, name=name)

fig.legend(ax.get_lines(), labels, ncol=3, loc="upper center")
plt.show()
```
