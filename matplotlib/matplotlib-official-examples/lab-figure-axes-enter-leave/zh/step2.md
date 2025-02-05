# 创建图形和坐标轴

我们将使用 `subplots` 函数创建一个包含两个子图（坐标轴）的图形。我们还将设置图形的标题。

```python
fig, axs = plt.subplots(2, 1)
fig.suptitle('Mouse Hover Over Figure or Axes to Trigger Events')
```
