# 使用线性方法插值数据

第二步是使用线性方法对数据进行插值。我们将创建一个规则间隔的四边形网格，然后使用线性三角形插值器（LinearTriInterpolator）方法对数据进行插值。最后，我们将绘制插值后的数据。

```python
# 插值到规则间隔的四边形网格。
z = np.cos(1.5 * x) * np.cos(1.5 * y)
xi, yi = np.meshgrid(np.linspace(0, 3, 20), np.linspace(0, 3, 20))

# 使用线性方法插值。
interp_lin = mtri.LinearTriInterpolator(triang, z)
zi_lin = interp_lin(xi, yi)

# 绘制插值后的数据。
plt.contourf(xi, yi, zi_lin)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("线性插值")
plt.show()
```
