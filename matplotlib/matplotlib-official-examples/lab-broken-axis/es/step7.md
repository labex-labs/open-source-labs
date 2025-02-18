# Ajustar las Marcas (Ticks)

Ahora ajustaremos las marcas (ticks) en el eje x. Movemos las marcas de la primera subfigura (subplot) hacia la parte superior utilizando `ax1.xaxis.tick_top`, eliminamos las etiquetas de las marcas en la primera subfigura con `ax1.tick_params(labeltop=False)` y mantenemos las etiquetas de las marcas en la segunda subfigura.

```python
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()
```
