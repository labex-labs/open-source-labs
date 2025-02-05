# 设置颜色映射和扩展设置

最后，我们将设置颜色映射和扩展设置。我们将使用`with_extremes`方法为低于和高于级别范围的值设置颜色。我们还将创建四个子图，以展示四种可能的`extend`设置：`'neither'`、`'both'`、`'min'`和`'max'`。

```python
# 设置颜色映射和扩展设置
extends = ["neither", "both", "min", "max"]
cmap = plt.colormaps["winter"].with_extremes(under="magenta", over="yellow")

# 创建具有不同扩展设置的子图
fig, axs = plt.subplots(2, 2, layout="constrained")
for ax, extend in zip(axs.flat, extends):
    cs = ax.contourf(X, Y, Z, levels, cmap=cmap, extend=extend, origin=origin)
    fig.colorbar(cs, ax=ax, shrink=0.9)
    ax.set_title("extend = %s" % extend)
    ax.locator_params(nbins=4)

# 显示图形
plt.show()
```
