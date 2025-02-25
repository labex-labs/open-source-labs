# Personalizar el gráfico

Podemos personalizar el gráfico agregando etiquetas, un título y ajustando las etiquetas de las marcas del eje x y la leyenda. También estableceremos el límite del eje y para asegurarnos de que toda nuestra data sea visible.

```python
ax.set_ylabel('Length (mm)')
ax.set_title('Penguin attributes by species')
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)
```
