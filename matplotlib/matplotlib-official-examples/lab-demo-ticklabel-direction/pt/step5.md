# Direção personalizada dos rótulos de marcação (tick label)

Nesta etapa, criaremos um subplot com a direção personalizada dos rótulos de marcação.

```python
ax = setup_axes(fig, 132)
ax.axis["left"].set_axis_direction("right")
ax.axis["bottom"].set_axis_direction("top")
ax.axis["right"].set_axis_direction("left")
ax.axis["top"].set_axis_direction("bottom")
```
