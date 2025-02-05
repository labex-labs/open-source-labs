# 创建三维曲面图

我们将为第一个子图创建一个三维曲面图。我们将使用NumPy来创建该图的数据。

```python
# 为三维曲面图创建数据
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# 绘制三维曲面图
surf = ax1.plot_surface(X, Y, Z, cmap='coolwarm', linewidth=0, antialiased=False)

# 为该图添加一个颜色条
fig.colorbar(surf, shrink=0.5, aspect=10)

# 设置z轴的范围
ax1.set_zlim(-1.01, 1.01)
```
