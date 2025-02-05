# 绘制3D曲面

在这一步中，我们将使用测试数据绘制3D曲面，并自定义图形的外观。

```python
# 绘制3D曲面
ax.plot_surface(X, Y, Z, edgecolor='royalblue', lw=0.5, rstride=8, cstride=8, alpha=0.3)

# 自定义图形的外观
ax.set(xlim=(-40, 40), ylim=(-40, 40), zlim=(-100, 100), xlabel='X', ylabel='Y', zlabel='Z')
```
