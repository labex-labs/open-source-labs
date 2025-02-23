# Agregar una elipse al gráfico

En este paso, agregaremos una elipse al gráfico. Utilizaremos la función `Ellipse` para crear la elipse y personalizaremos las propiedades de la elipse, como la posición, el ancho, el alto y el ángulo.

```python
ax = axs.flat[1]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
```
