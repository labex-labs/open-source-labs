# Definir os Rótulos dos Eixos

Definimos os rótulos dos eixos para os lados esquerdo e direito do gráfico usando a função `ax1.axis[]`. Também definimos a direção dos rótulos das marcas de escala (tick labels) usando a função `set_axis_direction()`.

```python
ax1.axis["left"].major_ticklabels.set_axis_direction("top")
ax1.axis["left"].label.set_text("Left label")

ax1.axis["right"].label.set_visible(True)
ax1.axis["right"].label.set_text("Right label")
ax1.axis["right"].label.set_axis_direction("left")
```
