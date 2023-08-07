# Define the on_press function

Next, we define a function called on_press that will adjust the z and y limits of the second window based on the location of a mouse click in the first window.

```python
def on_press(event):
    if event.button != 1:
        return
    x, y = event.xdata, event.ydata
    axzoom.set_xlim(x - 0.1, x + 0.1)
    axzoom.set_ylim(y - 0.1, y + 0.1)
    figzoom.canvas.draw()
```
