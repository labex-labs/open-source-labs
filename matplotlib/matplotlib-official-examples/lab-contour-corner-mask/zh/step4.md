# 创建图表

在这一步中，我们将使用 `contourf()` 函数创建掩码等高线图。我们将 `x`、`y` 和 `z` 数组传递给此函数，并根据我们要创建的图表类型将 `corner_mask` 参数设置为 `True` 或 `False`。

```python
corner_masks = [False, True]
fig, axs = plt.subplots(ncols=2)
for ax, corner_mask in zip(axs, corner_masks):
    cs = ax.contourf(x, y, z, corner_mask=corner_mask)
    ax.contour(cs, colors='k')
    ax.set_title(f'{corner_mask=}')

    # 绘制网格。
    ax.grid(c='k', ls='-', alpha=0.3)

    # 用红色圆圈指示掩码点。
    ax.plot(np.ma.array(x, mask=~mask), y, 'ro')

plt.show()
```
