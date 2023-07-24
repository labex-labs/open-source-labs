# Mouse Click Event

We can connect to mouse click events using the `button_press_event` method. In this example, we are disconnecting the mouse move event callback when the left mouse button is clicked.

```python
from matplotlib.backend_bases import MouseButton

def on_click(event):
    if event.button is MouseButton.LEFT:
        print('disconnecting callback')
        plt.disconnect(binding_id)

plt.connect('button_press_event', on_click)
```
