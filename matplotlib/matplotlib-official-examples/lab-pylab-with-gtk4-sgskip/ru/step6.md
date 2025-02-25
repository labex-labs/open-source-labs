# Обновляем метку координатами курсора

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```

Мы создаем функцию, которая обновляет метку координатами x и y курсора, когда он перемещается над графиками. Соединяем функцию с событием `motion_notify_event` холста.
