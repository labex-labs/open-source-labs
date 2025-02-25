# Quitar las etiquetas de las marcas de graduación

Podemos quitar las etiquetas de las marcas de graduación de un subgráfico específico modificando la visibilidad de las etiquetas utilizando el método `ax.get_xticklabels()`. En este ejemplo, quitaremos las etiquetas de las marcas de graduación en el eje x del segundo subgráfico.

```python
plt.tick_params('x', labelbottom=False)
```
