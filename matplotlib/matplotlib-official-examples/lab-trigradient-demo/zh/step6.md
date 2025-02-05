# 绘制三角剖分、电势等值线和矢量场

```python
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.use_sticky_edges = False
ax.margins(0.07)

ax.triplot(triang, color='0.8')

levels = np.arange(0., 1., 0.01)
ax.tricontour(tri_refi, z_test_refi, levels=levels, cmap='hot',
              linewidths=[2.0, 1.0, 1.0, 1.0])

ax.quiver(triang.x, triang.y, Ex/E_norm, Ey/E_norm,
          units='xy', scale=10., zorder=3, color='blue',
          width=0.007, headwidth=3., headlength=4.)

ax.set_title('Gradient Plot: Electrical Dipole')
plt.show()
```

解释：

- `fig` 和 `ax` 分别是图形和坐标轴对象。
- `ax.set_aspect` 设置坐标轴的纵横比。
- `ax.use_sticky_edges` 和 `ax.margins` 设置坐标轴的边距。
- `ax.triplot` 绘制三角剖分。
- `ax.tricontour` 绘制电势等值线。
- `ax.quiver` 绘制矢量场。
- `ax.set_title` 设置图形的标题。
