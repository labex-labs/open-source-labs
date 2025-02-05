# 创建一个子图

我们将创建一个子图来展示带颜色的线段。我们会使用 `matplotlib.pyplot` 中的 `subplots` 函数创建一个2x1的子图网格，并使用 `sharex` 和 `sharey` 参数在子图之间共享x轴和y轴。

```python
fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])
```
