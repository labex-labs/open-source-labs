# Create a hatched contour plot

We can create a hatched contour plot by specifying the `hatches` parameter in `ax.tricontourf`. We can also use a different colormap by specifying the `cmap` parameter.

```python
fig2, ax2 = plt.subplots()
ax2.set_aspect("equal")
tcf = ax2.tricontourf(
    triang,
    z,
    hatches=["*", "-", "/", "//", "\\", None],
    cmap="cividis"
)
fig2.colorbar(tcf)
ax2.tricontour(triang, z, linestyles="solid", colors="k", linewidths=2.0)
ax2.set_title("Hatched Contour plot of Delaunay triangulation")
```
