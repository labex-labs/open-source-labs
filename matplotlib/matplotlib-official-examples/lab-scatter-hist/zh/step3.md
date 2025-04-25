# 定义 scatter_hist 函数

我们需要定义`scatter_hist`函数，它接受 x 和 y 数据，以及三个坐标轴，一个用于散点图的主坐标轴，和两个边缘坐标轴。然后它将在所提供的坐标轴内创建散点图和直方图。

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
