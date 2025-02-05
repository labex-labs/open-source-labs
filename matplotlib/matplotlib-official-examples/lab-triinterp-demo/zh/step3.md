# 使用三次方法插值数据

第三步是使用三次方法对数据进行插值。我们将使用三次三角形插值器（CubicTriInterpolator）方法，并将 kind 参数设置为 'geom' 或'min_E'。最后，我们将绘制插值后的数据。

```python
# 使用 kind='geom' 的三次方法进行插值。
interp_cubic_geom = mtri.CubicTriInterpolator(triang, z, kind='geom')
zi_cubic_geom = interp_cubic_geom(xi, yi)

# 绘制插值后的数据。
plt.contourf(xi, yi, zi_cubic_geom)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("三次插值，kind='geom'")
plt.show()

# 使用 kind='min_E' 的三次方法进行插值。
interp_cubic_min_E = mtri.CubicTriInterpolator(triang, z, kind='min_E')
zi_cubic_min_E = interp_cubic_min_E(xi, yi)

# 绘制插值后的数据。
plt.contourf(xi, yi, zi_cubic_min_E)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("三次插值，kind='min_E'")
plt.show()
```
