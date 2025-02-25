# Crear las cuadrículas internas y las subtramas

En este paso, crearemos las cuadrículas internas y las subtramas utilizando `.GridSpec` anidados. Recorreremos cada celda de la cuadrícula externa y crearemos una cuadrícula de 3x3 para cada celda.

```python
for a in range(4):
    for b in range(4):
        # gridspec dentro de gridspec
        inner_grid = outer_grid[a, b].subgridspec(3, 3, wspace=0, hspace=0)
        axs = inner_grid.subplots()  # Crea todas las subtramas para la cuadrícula interna.
        for (c, d), ax in np.ndenumerate(axs):
            ax.plot(*squiggle_xy(a + 1, b + 1, c + 1, d + 1))
            ax.set(xticks=[], yticks=[])
```
