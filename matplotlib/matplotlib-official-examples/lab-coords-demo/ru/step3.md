# Событие нажатия кнопки мыши

Мы можем подключаться к событиям нажатия кнопки мыши с использованием метода `button_press_event`. В этом примере мы отключаем обратный вызов для события перемещения мыши, когда нажимается левая кнопка мыши.

```python
from matplotlib.backend_bases import MouseButton

def on_click(event):
    if event.button is MouseButton.LEFT:
        print('disconnecting callback')
        plt.disconnect(binding_id)

plt.connect('button_press_event', on_click)
```
