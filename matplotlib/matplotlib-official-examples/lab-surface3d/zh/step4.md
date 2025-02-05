# 绘制曲面

```python
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
```

我们使用 `plot_surface()` 函数绘制曲面。我们传入 `X`、`Y` 和 `Z` 值，以及设置为 `cm.coolwarm` 的 `cmap` 参数，以便使用 coolwarm 颜色映射为曲面着色。我们还将 `linewidth=0` 设置为移除线框，并将 `antialiased=False` 设置为使曲面不透明。
