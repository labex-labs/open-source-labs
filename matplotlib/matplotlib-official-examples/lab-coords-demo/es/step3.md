# Evento de clic del mouse

Podemos conectarnos a los eventos de clic del mouse utilizando el método `button_press_event`. En este ejemplo, estamos desconectando la devolución de llamada del evento de movimiento del mouse cuando se hace clic con el botón izquierdo del mouse.

```python
from matplotlib.backend_bases import MouseButton

def on_click(event):
    if event.button is MouseButton.LEFT:
        print('desconectando devolución de llamada')
        plt.disconnect(binding_id)

plt.connect('button_press_event', on_click)
```
