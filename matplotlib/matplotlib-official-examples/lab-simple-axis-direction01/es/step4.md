# Establecer las etiquetas de los ejes

Establecemos las etiquetas de los ejes para los lados izquierdo y derecho de la gráfica utilizando la función `ax1.axis[]`. También establecemos la dirección de las etiquetas de las marcas de graduación utilizando la función `set_axis_direction()`.

```python
ax1.axis["left"].major_ticklabels.set_axis_direction("top")
ax1.axis["left"].label.set_text("Etiqueta izquierda")

ax1.axis["right"].label.set_visible(True)
ax1.axis["right"].label.set_text("Etiqueta derecha")
ax1.axis["right"].label.set_axis_direction("left")
```
