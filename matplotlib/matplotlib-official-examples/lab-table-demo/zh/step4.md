# 创建配色方案

我们将使用`plt.cm.BuPu`函数为表格创建一种配色方案。我们将为各行使用浅蓝色和浅紫色的柔和色调。

```python
colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
```
