# 在网格上进行插值

我们通过在网格上进行插值来创建不规则间隔数据坐标的等高线图。我们首先使用 `np.linspace` 创建x和y的网格值。然后，我们使用 `tri.LinearTriInterpolator` 在由 (xi, yi) 定义的网格上对数据 (x, y) 进行线性插值。我们使用常规的 `axes.Axes.contour` 绘制插值后的数据。

```python
ngridx = 100
ngridy = 200
xi = np.linspace(-2.1, 2.1, ngridx)
yi = np.linspace(-2.1, 2.1, ngridy)

triang = tri.Triangulation(x, y)
interpolator = tri.LinearTriInterpolator(triang, z)
Xi, Yi = np.meshgrid(xi, yi)
zi = interpolator(Xi, Yi)

fig, ax1 = plt.subplots()
cntr1 = ax1.contourf(xi, yi, zi, levels=14, cmap="RdBu_r")
ax1.plot(x, y, 'ko', ms=3)
ax1.set(xlim=(-2, 2), ylim=(-2, 2))
ax1.set_title('Contour Plot of Irregularly Spaced Data Interpolated on a Grid')
fig.colorbar(cntr1, ax=ax1)
plt.show()
```
