# Update Label Text on Mouse Movement

We will update the label text to display the x,y coordinates of the mouse when it is dragged over the axis. We create a function to update the label text and connect it to the `motion_notify_event` using the `mpl_connect()` method.

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```
