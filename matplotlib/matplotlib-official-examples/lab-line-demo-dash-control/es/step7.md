# Establecer otros atributos del trazo usando métodos relevantes

Otros atributos del trazo también pueden establecerse usando métodos relevantes como `~.Line2D.set_dash_joinstyle()`, `~.Line2D.set_dash_joinstyle()` y `~.Line2D.set_gapcolor()`. En este ejemplo, usaremos los parámetros `dashes` y `gapcolor` para establecer la secuencia de trazos y el color alternante para `line3`.

```python
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')
```
