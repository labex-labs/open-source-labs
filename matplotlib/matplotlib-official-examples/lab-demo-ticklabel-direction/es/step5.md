# Dirección personalizada de las etiquetas de los ejes

En este paso, crearemos un subgráfico con una dirección personalizada para las etiquetas de los ejes.

```python
ax = setup_axes(fig, 132)
ax.axis["left"].set_axis_direction("right")
ax.axis["bottom"].set_axis_direction("top")
ax.axis["right"].set_axis_direction("left")
ax.axis["top"].set_axis_direction("bottom")
```
