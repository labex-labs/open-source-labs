# 设置图形

使用 `plt.figure()` 和 `add_gridspec()` 设置图形。该图形将有一个 2 列和 n 行的网格，其中 n 是箭头样式的数量。网格中的每个单元格将包含一种箭头样式及其默认参数。

```python
ncol = 2
nrow = (len(styles) + 1) // ncol
axs = (plt.figure(figsize=(4 * ncol, 1 + nrow))
     .add_gridspec(1 + nrow, ncol,
                    wspace=.7, left=.1, right=.9, bottom=0, top=1).subplots())
for ax in axs.flat:
    ax.set_axis_off()
for ax in axs[0, :]:
    ax.text(0,.5, "arrowstyle",
            transform=ax.transAxes, size="large", color="tab:blue",
            horizontalalignment="center", verticalalignment="center")
    ax.text(.35,.5, "default parameters",
            transform=ax.transAxes,
            horizontalalignment="left", verticalalignment="center")
```
