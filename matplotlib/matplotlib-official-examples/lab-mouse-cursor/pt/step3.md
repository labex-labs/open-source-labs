# Definir o cursor ao passar o mouse

Precisamos definir o cursor para o cursor alternativo quando o usuário passa o mouse sobre um subplot. Conseguimos isso usando o evento `motion_notify_event` e a função `set_cursor()`.

```python
def hover(event):
    if fig.canvas.widgetlock.locked():
        # Don't do anything if the zoom/pan tools have been enabled.
        return

    fig.canvas.set_cursor(
        event.inaxes.cursor_to_use if event.inaxes else Cursors.POINTER)

fig.canvas.mpl_connect('motion_notify_event', hover)
```
