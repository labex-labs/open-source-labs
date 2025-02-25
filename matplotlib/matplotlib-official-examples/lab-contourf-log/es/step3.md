# Crear el gráfico

Usaremos la función `contourf` para crear un gráfico de contorno relleno con una escala de colores logarítmica:

```python
fig, ax = plt.subplots()
cs = ax.contourf(X, Y, z, locator=ticker.LogLocator(), cmap=cm.PuBu_r)

cbar = fig.colorbar(cs)

plt.show()
```
