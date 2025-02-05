# 创建三维表面图

现在我们可以创建三维表面图了。我们首先创建一个图形，并使用 `projection='3d'` 参数添加一个子图。然后，我们使用 `plot_surface()` 函数，根据上一步创建的数据绘制表面。

```python
# 绘制表面
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z)
```
