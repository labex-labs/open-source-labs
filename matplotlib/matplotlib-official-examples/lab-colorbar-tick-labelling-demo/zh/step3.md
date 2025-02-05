# 自定义垂直颜色条上的刻度标签

接下来，我们将自定义垂直颜色条上的刻度标签。我们将使用 `colorbar` 创建一个颜色条，并使用 `ticks` 参数指定刻度位置。然后，我们将在颜色条对象的 `ax` 属性上使用 `set_yticklabels` 设置刻度标签。

```python
# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[-1, 0, 1])
cbar.ax.set_yticklabels(['< -1', '0', '> 1'])  # vertically oriented colorbar
```
