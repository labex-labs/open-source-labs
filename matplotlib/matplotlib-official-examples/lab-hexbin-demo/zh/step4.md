# 添加对数颜色刻度

我们可以通过在 `hexbin()` 中设置 `bins='log'` 为六边形分箱图添加对数颜色刻度。

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("With a log color scale")

cb = fig.colorbar(hb, ax=ax, label='log10(N)')
```
