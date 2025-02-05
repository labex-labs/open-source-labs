# 使用默认单位创建柱状图

在这一步中，我们将使用 Matplotlib 的 `bar` 方法，以默认单位创建柱状图。我们将使用 `bottom` 参数将柱子的底部设置为 0。

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].bar(cms, cms, bottom=bottom)
```
