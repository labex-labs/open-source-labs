# Evento de Clique do Mouse

Podemos nos conectar aos eventos de clique do mouse usando o método `button_press_event`. Neste exemplo, estamos desconectando o callback do evento de movimento do mouse quando o botão esquerdo do mouse é clicado.

```python
from matplotlib.backend_bases import MouseButton

def on_click(event):
    if event.button is MouseButton.LEFT:
        print('disconnecting callback')
        plt.disconnect(binding_id)

plt.connect('button_press_event', on_click)
```
