# Создайте штрихованную карту контуров

Мы можем создать штрихованную карту контуров, указав параметр `hatches` в `ax.tricontourf`. Мы также можем использовать другую цветовую карту, указав параметр `cmap`.

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
