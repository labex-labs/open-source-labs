# scatter_hist 関数の定義

`scatter_hist`関数を定義する必要があります。この関数は、x と y のデータと、3 つの軸（散布図用の主軸と 2 つの余白軸）を引数に取り、与えられた軸の中に散布図とヒストグラムを作成します。

```python
def scatter_hist(x, y, ax, ax_histx, ax_histy):
    # Remove labels from the histograms
    ax_histx.tick_params(axis="x", labelbottom=False)
    ax_histy.tick_params(axis="y", labelleft=False)

    # Create the scatter plot
    ax.scatter(x, y)

    # Determine nice limits by hand
    binwidth = 0.25
    xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
    lim = (int(xymax/binwidth) + 1) * binwidth

    bins = np.arange(-lim, lim + binwidth, binwidth)
    ax_histx.hist(x, bins=bins)
    ax_histy.hist(y, bins=bins, orientation='horizontal')
```
