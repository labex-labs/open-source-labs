# Personalizar o Gráfico

Podemos personalizar nosso gráfico alterando a cor da grade e adicionando uma legenda. Neste exemplo, moveremos a legenda ligeiramente para longe do centro do gráfico para evitar sobreposição.

```python
ax.tick_params(grid_color="palegoldenrod")
angle = np.deg2rad(67.5)
ax.legend(loc="lower left",
          bbox_to_anchor=(.5 + np.cos(angle)/2, .5 + np.sin(angle)/2))
```
