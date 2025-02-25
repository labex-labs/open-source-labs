# Crear el gráfico

Ahora que tenemos nuestros datos, podemos crear el gráfico de contorno. En este ejemplo, usaremos la función `plot_wireframe()` para crear el gráfico.

```python
# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)
```
