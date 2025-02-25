# Erstellen eines durchgestrichenen Konturplots

Wir können einen durchgestrichenen Konturplot erstellen, indem wir den Parameter `hatches` in `ax.tricontourf` angeben. Wir können auch eine andere Farbskala verwenden, indem wir den Parameter `cmap` angeben.

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
