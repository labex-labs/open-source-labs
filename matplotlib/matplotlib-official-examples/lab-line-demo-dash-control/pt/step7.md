# Definir outros atributos do traço usando métodos relevantes

Outros atributos do traço também podem ser definidos usando métodos relevantes como `~.Line2D.set_dash_joinstyle()`, `~.Line2D.set_dash_joinstyle()` e `~.Line2D.set_gapcolor()`. Neste exemplo, usaremos os parâmetros `dashes` e `gapcolor` para definir a sequência de traços e a cor alternada para `line3`.

```python
line3, = ax.plot(x, y - 0.4, dashes=[4, 4], gapcolor='tab:pink',
                 label='Using the dashes and gapcolor parameters')
```
