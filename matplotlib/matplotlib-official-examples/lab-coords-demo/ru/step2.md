# Событие перемещения мыши

Мы можем подключаться к событиям перемещения мыши с использованием метода `motion_notify_event`. В этом примере мы выводим координаты x и y данных и координаты x и y пикселей, когда мышь движется по графику.

```python
def on_move(event):
    if event.inaxes:
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')

binding_id = plt.connect('motion_notify_event', on_move)
```
