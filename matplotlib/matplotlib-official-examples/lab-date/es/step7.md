# Formatear manualmente las etiquetas de los ticks

Formatearemos las etiquetas de los ticks en el tercer subgráfico manualmente utilizando `DateFormatter` para formatear las fechas con las cadenas de formato documentadas en `datetime.date.strftime`.

```python
ax = axs[2]
ax.set_title('Manual DateFormatter', loc='left', y=0.85, x=0.02, fontsize='medium')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
for label in ax.get_xticklabels(which='major'):
    label.set(rotation=30, horizontalalignment='right')
```
