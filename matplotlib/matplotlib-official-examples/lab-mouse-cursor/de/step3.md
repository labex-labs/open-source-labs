# Setzen des Cursors beim Hovern

Wir müssen den Cursor auf den alternativen Cursor setzen, wenn der Benutzer über einem Subplot hoviert. Dies erreichen wir mit dem Ereignis `motion_notify_event` und der Funktion `set_cursor()`.

```python
def hover(event):
    if fig.canvas.widgetlock.locked():
        # Don't do anything if the zoom/pan tools have been enabled.
        return

    fig.canvas.set_cursor(
        event.inaxes.cursor_to_use if event.inaxes else Cursors.POINTER)

fig.canvas.mpl_connect('motion_notify_event', hover)
```
