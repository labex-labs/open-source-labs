# 自定义子图

我们通过将底部子图的背景颜色设置为黑色、设置 x 轴刻度并为每个子图添加标题来进行自定义。

```python
axs[1, icol].set_facecolor('k')
axs[1, icol].xaxis.set_ticks(np.arange(0, 10, 2))
axs[0, icol].set_title(f'line widths (pts): {lwx:g}, {lwy:g}',
                       fontsize='medium')
```
