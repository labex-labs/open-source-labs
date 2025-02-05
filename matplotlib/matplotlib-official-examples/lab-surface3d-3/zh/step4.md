# 创建表面图

在这一步中，我们将使用取自我们创建的数组的面颜色来创建表面图。我们还将自定义 z 轴。

```python
# 创建表面图
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0)

# 自定义 z 轴
ax.set_zlim(-1, 1)
ax.zaxis.set_major_locator(LinearLocator(6))

# 显示图形
plt.show()
```
