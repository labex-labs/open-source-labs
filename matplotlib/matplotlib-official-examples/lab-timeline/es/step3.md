# Formateando la gráfica

Ahora, formatearemos la gráfica agregando etiquetas para los ejes x e y, configurando el localizador y formateador principales del eje x, y eliminando el eje y y las espinas. Aquí está el código para formatear la gráfica:

```python
# format x-axis with 4-month intervals
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y-axis and spines
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)
plt.show()
```
