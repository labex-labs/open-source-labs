# Formatear las etiquetas de los ticks con el formateador conciso

Formatearemos las etiquetas de los ticks en el segundo subgráfico utilizando el formateador conciso.

```python
ax = axs[1]
ax.set_title('ConciseFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
```
