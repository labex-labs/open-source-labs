# Crear un diagrama de dispersión en un eje polar con origen desplazado

Podemos crear un diagrama de dispersión en un eje polar con un origen desplazado estableciendo los métodos `set_rorigin()` y `set_theta_zero_location()` del objeto `PolarAxes`. Estableceremos el radio del origen en `-2.5` y la ubicación del cero de theta en `'W'` con un desplazamiento de `10`.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_rorigin(-2.5)
ax.set_theta_zero_location('W', offset=10)
```
