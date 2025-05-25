# 큐빅 방법 (Cubic Method) 을 사용하여 데이터 보간

세 번째 단계는 큐빅 방법 (cubic method) 을 사용하여 데이터를 보간하는 것입니다. kind 매개변수를 'geom' 또는 'min_E'로 설정하여 CubicTriInterpolator 메서드를 사용합니다. 마지막으로 보간된 데이터를 플롯 (plot) 합니다.

```python
# Interpolate using cubic method with kind=geom.
interp_cubic_geom = mtri.CubicTriInterpolator(triang, z, kind='geom')
zi_cubic_geom = interp_cubic_geom(xi, yi)

# Plot the interpolated data.
plt.contourf(xi, yi, zi_cubic_geom)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Cubic interpolation, kind='geom'")
plt.show()

# Interpolate using cubic method with kind=min_E.
interp_cubic_min_E = mtri.CubicTriInterpolator(triang, z, kind='min_E')
zi_cubic_min_E = interp_cubic_min_E(xi, yi)

# Plot the interpolated data.
plt.contourf(xi, yi, zi_cubic_min_E)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Cubic interpolation, kind='min_E'")
plt.show()
```
