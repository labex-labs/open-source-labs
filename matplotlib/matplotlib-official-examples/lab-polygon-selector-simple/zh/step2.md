# 以编程方式创建多边形

要以编程方式创建多边形，我们需要创建一个 `Figure` 对象和一个 `Axes` 对象。然后，我们可以创建一个 `PolygonSelector` 对象并向其添加顶点。最后，我们可以在 `Axes` 上绘制多边形。

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

# 添加三个顶点
selector.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# 绘制多边形
ax.add_patch(plt.Polygon(selector.verts, alpha=0.3))
plt.show()
```
