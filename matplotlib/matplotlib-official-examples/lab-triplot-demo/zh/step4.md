# 绘制Delaunay三角剖分

我们将使用 `triplot` 函数绘制三角剖分图。

```python
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
ax1.triplot(triang, 'bo-', lw=1)
ax1.set_title('Triplot of Delaunay Triangulation')
```
