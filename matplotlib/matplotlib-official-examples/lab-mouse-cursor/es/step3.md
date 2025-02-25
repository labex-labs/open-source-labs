# Establecer el cursor al pasar el cursor

Debemos establecer el cursor al cursor alternativo cuando el usuario pasa el cursor sobre una subtrama. Lo conseguimos utilizando el evento `motion_notify_event` y la función `set_cursor()`.

```python
def hover(event):
    if fig.canvas.widgetlock.locked():
        # Don't do anything if the zoom/pan tools have been enabled.
        return

    fig.canvas.set_cursor(
        event.inaxes.cursor_to_use if event.inaxes else Cursors.POINTER)

fig.canvas.mpl_connect('motion_notify_event', hover)
```
