# 绘制用户指定的三角剖分

我们将使用 `triplot` 函数绘制用户指定的三角剖分。

```python
fig2, ax2 = plt.subplots()
ax2.set_aspect('equal')
ax2.triplot(x, y, triangles, 'go-', lw=1.0)
ax2.set_title('Triplot of User-Specified Triangulation')
ax2.set_xlabel('Longitude (degrees)')
ax2.set_ylabel('Latitude (degrees)')
```
