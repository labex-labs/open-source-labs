# Set Colormap and Extend Settings

Finally, we will set the colormap and extend settings. We will use the `with_extremes` method to set the colors for values below and above the range of levels. We will also create four subplots to show the four possible `extend` settings: `'neither'`, `'both'`, `'min'`, and `'max'`.

```python
# Set colormap and extend settings
extends = ["neither", "both", "min", "max"]
cmap = plt.colormaps["winter"].with_extremes(under="magenta", over="yellow")

# Create subplots with different extend settings
fig, axs = plt.subplots(2, 2, layout="constrained")
for ax, extend in zip(axs.flat, extends):
    cs = ax.contourf(X, Y, Z, levels, cmap=cmap, extend=extend, origin=origin)
    fig.colorbar(cs, ax=ax, shrink=0.9)
    ax.set_title("extend = %s" % extend)
    ax.locator_params(nbins=4)

# Show plot
plt.show()
```
