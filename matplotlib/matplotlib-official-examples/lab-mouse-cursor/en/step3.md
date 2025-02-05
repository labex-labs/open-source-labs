# Set the cursor on hover

We need to set the cursor to the alternative cursor when the user hovers over a subplot. We achieve this using the `motion_notify_event` event and the `set_cursor()` function.

```python
def hover(event):
    if fig.canvas.widgetlock.locked():
        # Don't do anything if the zoom/pan tools have been enabled.
        return

    fig.canvas.set_cursor(
        event.inaxes.cursor_to_use if event.inaxes else Cursors.POINTER)

fig.canvas.mpl_connect('motion_notify_event', hover)
```
