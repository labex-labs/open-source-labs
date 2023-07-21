# Update the label with cursor coordinates

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```

We create a function that updates the label with the x and y coordinates of the cursor when it moves over the plots. We connect the function to the `motion_notify_event` of the canvas.
