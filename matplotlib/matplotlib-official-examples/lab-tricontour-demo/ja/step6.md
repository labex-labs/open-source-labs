# 色なしでラベル付きのハッチングパターンを生成する

`ax.tricontourf` の `colors` パラメータを `"none"` に指定することで、色なしでラベル付きのハッチングパターンを生成できます。また、`ContourSet.legend_elements` を使用してコントアーセットの凡例を作成することもできます。

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
