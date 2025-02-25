# Personalizar el gráfico

Podemos personalizar nuestro gráfico cambiando el color de la cuadrícula y agregando una leyenda. En este ejemplo, movemos la leyenda ligeramente alejada del centro del gráfico para evitar superposición.

```python
ax.tick_params(grid_color="palegoldenrod")
angle = np.deg2rad(67.5)
ax.legend(loc="lower left",
          bbox_to_anchor=(.5 + np.cos(angle)/2,.5 + np.sin(angle)/2))
```
