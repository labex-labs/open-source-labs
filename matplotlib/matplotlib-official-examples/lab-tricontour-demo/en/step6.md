# Generate hatching patterns labeled with no color

We can generate hatching patterns labeled with no color by specifying the `colors` parameter as `"none"` in `ax.tricontourf`. We can also create a legend for the contour set using `ContourSet.legend_elements`.

```python
fig3, ax3 = plt.subplots()
n_levels = 7
tcf = ax3.tricontourf(
    triang,
    z,
    n_levels,
    colors="none",
    hatches=[".", "/", "\\", None, "\\\\", "*"],
)
ax3.tricontour(triang, z, n_levels, colors="black", linestyles="-")

artists, labels = tcf.legend_elements(str_format="{:2.1f}".format)
ax3.legend(artists, labels, handleheight=2, framealpha=1)
```
