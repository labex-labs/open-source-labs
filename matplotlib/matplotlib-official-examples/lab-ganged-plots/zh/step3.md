# 创建子图

我们使用Matplotlib中的 `subplots` 函数创建三个子图。我们将 `sharex` 参数设置为 `True`，以确保子图共享一个公共x轴。我们还使用 `subplots_adjust` 函数去除子图之间的垂直间距。

```python
fig, axs = plt.subplots(3, 1, sharex=True)
fig.subplots_adjust(hspace=0)
```
