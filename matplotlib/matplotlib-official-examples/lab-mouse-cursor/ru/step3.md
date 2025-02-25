# Настраиваем курсор при наведении

Нам нужно установить курсор на альтернативный, когда пользователь наведет указатель мыши на подграфик. Мы достигаем этого с использованием события `motion_notify_event` и функции `set_cursor()`.

```python
def hover(event):
    if fig.canvas.widgetlock.locked():
        # Don't do anything if the zoom/pan tools have been enabled.
        return

    fig.canvas.set_cursor(
        event.inaxes.cursor_to_use if event.inaxes else Cursors.POINTER)

fig.canvas.mpl_connect('motion_notify_event', hover)
```
