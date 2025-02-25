# Crear un diagrama de dispersión en un eje polar limitado a un sector

Podemos crear un diagrama de dispersión en un eje polar limitado a un sector estableciendo los métodos `set_thetamin()` y `set_thetamax()` del objeto `PolarAxes`. Estableceremos los límites inicial y final de theta en `45` y `135`, respectivamente.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

ax.set_thetamin(45)
ax.set_thetamax(135)
```
