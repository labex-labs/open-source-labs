# 创建带阴影线的等高线图

我们可以通过在 `ax.tricontourf` 中指定 `hatches` 参数来创建带阴影线的等高线图。我们还可以通过指定 `cmap` 参数来使用不同的颜色映射。

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
