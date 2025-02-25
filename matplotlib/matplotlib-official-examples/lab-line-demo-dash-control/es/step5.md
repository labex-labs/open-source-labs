# Modificar la secuencia de trazos usando `.Line2D.set_dashes()`

Podemos modificar la secuencia de trazos usando `.Line2D.set_dashes()`. En este ejemplo, modificamos la secuencia de trazos para `line1` para crear un patrón de trazos de línea de 2pt, ruptura de 2pt, línea de 10pt y ruptura de 2pt. También establecemos el estilo de tapón en 'round' usando `line1.set_dash_capstyle()`.

```python
line1, = ax.plot(x, y, label='Using set_dashes() and set_dash_capstyle()')
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break.
line1.set_dash_capstyle('round')
```
