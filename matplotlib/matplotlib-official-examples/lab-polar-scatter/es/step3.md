# Crear un diagrama de dispersión en un eje polar

Crearemos un diagrama de dispersión en un eje polar utilizando la función `plt.scatter()`. Estableceremos el parámetro `proyección` en `'polar'` y pasaremos los valores de radio, ángulo, color y área como parámetros.

```python
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
```
