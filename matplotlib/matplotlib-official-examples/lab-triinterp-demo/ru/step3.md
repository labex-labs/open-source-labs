# Интерполяция данных методом кубической интерполяции

Третий шаг - интерполировать данные методом кубической интерполяции. Мы будем использовать метод CubicTriInterpolator с параметром kind, установленным на 'geom' или'min_E'. Наконец, мы построим график интерполированных данных.

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
