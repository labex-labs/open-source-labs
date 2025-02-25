# Интерполяция данных методом линейной интерполяции

Вторым шагом является интерполяция данных методом линейной интерполяции. Мы создадим равномерно разнесенную квадратную сетку и затем используем метод LinearTriInterpolator для интерполяции данных. Наконец, мы построим график интерполированных данных.

```python
# Interpolate to regularly-spaced quad grid.
z = np.cos(1.5 * x) * np.cos(1.5 * y)
xi, yi = np.meshgrid(np.linspace(0, 3, 20), np.linspace(0, 3, 20))

# Interpolate using linear method.
interp_lin = mtri.LinearTriInterpolator(triang, z)
zi_lin = interp_lin(xi, yi)

# Plot the interpolated data.
plt.contourf(xi, yi, zi_lin)
plt.plot(xi, yi, 'k-', lw=0.5, alpha=0.5)
plt.plot(xi.T, yi.T, 'k-', lw=0.5, alpha=0.5)
plt.title("Linear interpolation")
plt.show()
```
