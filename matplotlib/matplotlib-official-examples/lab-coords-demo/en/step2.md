# Mouse Move Event

We can connect to mouse move events using the `motion_notify_event` method. In this example, we are printing the x and y data coordinates and x and y pixel coordinates when the mouse moves over the plot.

```python
def on_move(event):
    if event.inaxes:
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')

binding_id = plt.connect('motion_notify_event', on_move)
```
