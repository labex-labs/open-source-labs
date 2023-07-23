# Customize tick labels on the vertical colorbar

Next, we will customize the tick labels on the vertical colorbar. We will create a colorbar using `colorbar` and specify the tick locations using the `ticks` parameter. We will then set the tick labels using `set_yticklabels` on the `ax` attribute of the colorbar object.

```python
# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[-1, 0, 1])
cbar.ax.set_yticklabels(['< -1', '0', '> 1'])  # vertically oriented colorbar
```
