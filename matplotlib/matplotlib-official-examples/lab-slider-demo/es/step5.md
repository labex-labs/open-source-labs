# Crear la función de actualización

Ahora crearemos la función que actualizará la onda sinusoidal cada vez que ajustemos los deslizadores. La función tomará los valores de los deslizadores de amplitud y frecuencia y actualizará la onda sinusoidal en consecuencia.

```python
def update(val):
    line.set_ydata(f(t, amp_slider.val, freq_slider.val))
    fig.canvas.draw_idle()
```
