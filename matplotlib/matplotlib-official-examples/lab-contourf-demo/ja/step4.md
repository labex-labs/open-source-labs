# カラーマップと拡張設定の設定

最後に、カラーマップと拡張設定を設定します。`with_extremes`メソッドを使って、レベルの範囲より下と上の値の色を設定します。また、4 つのサブプロットを作成して、4 つの可能な`extend`設定：`'neither'`、`'both'`、`'min'`、および`'max'`を表示します。

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
