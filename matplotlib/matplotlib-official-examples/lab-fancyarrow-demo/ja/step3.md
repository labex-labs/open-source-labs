# グラフを設定する

`plt.figure()` と `add_gridspec()` を使ってグラフを設定します。グラフは 2 列と n 行のグリッドになっており、n は矢印スタイルの数です。グリッドの各セルには矢印スタイルとその既定のパラメータが含まれます。

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
