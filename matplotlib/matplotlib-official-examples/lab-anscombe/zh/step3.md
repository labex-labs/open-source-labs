# 创建带有子图的图形

现在我们将创建一个带有四个子图的图形，每个数据集对应一个子图。我们还将为所有子图设置相同的 x 轴和 y 轴范围。

```python
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(6, 6),
                        gridspec_kw={'wspace': 0.08, 'hspace': 0.08})
axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
axs[0, 0].set(xticks=(0, 10, 20), yticks=(4, 8, 12))
```
