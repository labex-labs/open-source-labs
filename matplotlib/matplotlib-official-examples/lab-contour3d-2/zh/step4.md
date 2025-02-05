# 创建等高线图

现在我们将使用 `contour()` 函数创建等高线图。我们将传入 `X`、`Y` 和 `Z` 数据，并设置 `extend3d=True` 以便将曲线垂直扩展为“带状”。我们还将颜色映射设置为 `cm.coolwarm` 以获得不错的配色方案。

```python
ax.contour(X, Y, Z, extend3d=True, cmap=cm.coolwarm)
```
