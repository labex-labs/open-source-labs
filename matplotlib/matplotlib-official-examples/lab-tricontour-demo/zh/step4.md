# 创建伪彩色图

我们将使用 `ax.tricontourf` 和 `fig.colorbar` 创建一个伪彩色图。

```python
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tcf = ax1.tricontourf(triang, z)
fig1.colorbar(tcf)
ax1.tricontour(triang, z, colors='k')
ax1.set_title('Contour plot of Delaunay triangulation')
```
