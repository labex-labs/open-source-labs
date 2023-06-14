# Set up Interactivity

We need to set up interactivity to update the triangle under the cursor. We will use the `motion_notify_event` to detect when the mouse is moved over the plot. We will create a function `on_mouse_move()` that will get the triangle under the cursor using the TriFinder object, update the polygon with the vertices of the triangle, and update the plot title with the index of the triangle.

```python
def on_mouse_move(event):
    if event.inaxes is None:
        tri = -1
    else:
        tri = trifinder(event.xdata, event.ydata)
    update_polygon(tri)
    ax.set_title(f'Triangle {tri}')
    event.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
```
