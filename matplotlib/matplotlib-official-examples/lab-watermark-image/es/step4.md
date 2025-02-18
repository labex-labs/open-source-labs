# Superponer la imagen

Para superponer la imagen en el gráfico, podemos utilizar el método `figimage` de la clase `matplotlib.figure.Figure`. Necesitamos especificar la imagen, la posición de la imagen en el gráfico, el orden z (para mover la imagen hacia la parte frontal) y el valor alpha (para hacer la imagen semi-transparente).

```python
fig.figimage(im, 25, 25, zorder=3, alpha=.7)
```
