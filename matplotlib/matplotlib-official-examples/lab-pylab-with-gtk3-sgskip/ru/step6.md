# Обновление текста метки при движении мыши

Мы обновим текст метки для отображения координат x,y мыши, когда она перетаскивается по оси. Мы создаем функцию для обновления текста метки и подключаем ее к событию `motion_notify_event` с использованием метода `mpl_connect()`.

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```
