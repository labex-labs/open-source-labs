# 绘制曲面

在这一步中，我们将使用 Matplotlib 的 `plot_surface()` 函数绘制曲面。我们将使用 `YlGnBu_r` 颜色映射来设置曲面的颜色。

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
```
