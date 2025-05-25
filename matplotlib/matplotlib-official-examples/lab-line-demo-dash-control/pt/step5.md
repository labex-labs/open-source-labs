# Modificar a sequência de traços usando `.Line2D.set_dashes()`

Podemos modificar a sequência de traços usando `.Line2D.set_dashes()`. Neste exemplo, modificamos a sequência de traços para `line1` para criar um padrão de traços de linha de 2pt, intervalo de 2pt, linha de 10pt e intervalo de 2pt. Também definimos o estilo da extremidade (cap style) para 'round' usando `line1.set_dash_capstyle()`.

```python
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break.
line1.set_dash_capstyle('round')
```
