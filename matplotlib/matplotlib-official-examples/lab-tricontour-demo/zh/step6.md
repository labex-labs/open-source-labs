# 生成无颜色标注的阴影图案

我们可以通过在 `ax.tricontourf` 中将 `colors` 参数指定为 `"none"` 来生成无颜色标注的阴影图案。我们还可以使用 `ContourSet.legend_elements` 为等高线集创建一个图例。

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
