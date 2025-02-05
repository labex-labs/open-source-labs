# 创建多边形并添加到绘图中

我们使用 Matplotlib 的 `PolyCollection` 函数创建多边形，并将它们添加到绘图中。

```python
poly = PolyCollection(verts, facecolors=facecolors, alpha=.7)
ax.add_collection3d(poly, zs=lambdas, zdir='y')
```
