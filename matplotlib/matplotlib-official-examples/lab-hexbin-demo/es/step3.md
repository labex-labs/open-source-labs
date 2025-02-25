# Crear el diagrama de contenedores hexagonales

Crearemos el diagrama de contenedores hexagonales utilizando `matplotlib.pyplot.hexbin()`.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("Hexagon binning")

cb = fig.colorbar(hb, ax=ax, label='counts')
```

Aquí, establecemos el tamaño de la cuadrícula en 50 y la paleta de colores en 'inferno'. También agregamos una barra de colores para mostrar la cuenta de puntos de datos dentro de cada hexágono.
