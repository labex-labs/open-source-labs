# Mausklickerevent

Wir können uns an Mausklickerevents über die Methode `button_press_event` anmelden. In diesem Beispiel trennen wir den Callback für das Mausbewegungsevent, wenn die linke Maustaste gedrückt wird.

```python
from matplotlib.backend_bases import MouseButton

def on_click(event):
    if event.button is MouseButton.LEFT:
        print('disconnecting callback')
        plt.disconnect(binding_id)

plt.connect('button_press_event', on_click)
```
