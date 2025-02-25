# Gráfico de sombreados sin color con leyenda

En este paso, crearemos un gráfico de sombreados sin color y agregaremos una leyenda. Usaremos la función `contour` para crear las líneas de contorno y la función `contourf` para especificar los sombreados sin color.

```python
fig2, ax2 = plt.subplots()
n_levels = 6
ax2.contour(x, y, z, n_levels, colors='black', linestyles='-')
cs = ax2.contourf(x, y, z, n_levels, colors='none',
                  hatches=['.', '/', '\\', None, '\\\\', '*'],
                  extend='lower')

# create a legend for the contour set
artists, labels = cs.legend_elements(str_format='{:2.1f}'.format)
ax2.legend(artists, labels, handleheight=2, framealpha=1)
```
