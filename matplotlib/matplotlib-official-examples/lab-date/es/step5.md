# Formatear las etiquetas de los ticks con el formateador predeterminado

Formatearemos las etiquetas de los ticks en el primer subgráfico utilizando el formateador predeterminado.

```python
ax = axs[0]
ax.set_title('DefaultFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
ax.xaxis.set_minor_locator(mdates.MonthLocator())
```
