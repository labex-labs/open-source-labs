# ハッチ付きコントアープロットを作成する

`ax.tricontourf` の `hatches` パラメータを指定することで、ハッチ付きコントアープロットを作成できます。また、`cmap` パラメータを指定することで別のカラーマップを使用できます。

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
