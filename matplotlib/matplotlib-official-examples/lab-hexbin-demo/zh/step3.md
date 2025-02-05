# 创建六边形分箱图

我们将使用 `matplotlib.pyplot.hexbin()` 创建六边形分箱图。

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("Hexagon binning")

cb = fig.colorbar(hb, ax=ax, label='counts')
```

在这里，我们将网格大小设置为 50，并将颜色映射设置为 'inferno'。我们还添加了一个颜色条来显示每个六边形内的数据点数量。
