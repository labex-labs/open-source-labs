# Estableciendo las etiquetas de los ticks

Por defecto, las etiquetas de los ticks con valores negativos se representan utilizando un signo menos Unicode en lugar de un guión ASCII. Sin embargo, podemos cambiar este comportamiento estableciendo `axes.unicode_minus` en `False`.

```python
plt.rcParams['axes.unicode_minus'] = False
```
