# Crear la función de actualización

En este paso, creará la función de actualización para los deslizadores. Esta función actualizará la gráfica cuando se cambien los valores de los deslizadores.

```python
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()
```
