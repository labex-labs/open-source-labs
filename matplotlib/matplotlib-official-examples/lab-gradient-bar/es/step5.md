# Crear la gráfica

Ahora, podemos crear la gráfica. Primero crearemos una figura y un objeto de ejes. Luego estableceremos los límites x e y de los ejes. Crearemos un fondo de degradado utilizando la función `gradient_image()`. Finalmente, crearemos un conjunto de datos aleatorios y usaremos la función `gradient_bar()` para crear el gráfico de barras.

```python
fig, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(0, 1))

# imagen de fondo
gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes,
               cmap=plt.cm.RdYlGn, cmap_range=(0.2, 0.8), alpha=0.5)

N = 10
x = np.arange(N) + 0.15
y = np.random.rand(N)
gradient_bar(ax, x, y, width=0.7)
plt.show()
```
