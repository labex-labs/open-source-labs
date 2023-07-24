# Define the Keypress Event Function

Next, we define a function `on_press` that will be called when a key is pressed. This function takes an `event` parameter which contains information about the key that was pressed. In this example, we will toggle the visibility of the x-label when the 'x' key is pressed.

```python
def on_press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()
```
