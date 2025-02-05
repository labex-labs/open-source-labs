# Define Function to Update Title

Define the function to update the title of the figure with the current time.

```python
def update_title(axes):
    axes.set_title(datetime.now())
    axes.figure.canvas.draw()
```
