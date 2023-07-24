# Define a function to update the second axis

We will define a closure function to register as a callback to update the second axis according to the first axis.

```python
def convert_ax_c_to_celsius(ax_f):
    """
    Update second axis according to first axis.
    """
    y1, y2 = ax_f.get_ylim()
    ax_c.set_ylim(fahrenheit2celsius(y1), fahrenheit2celsius(y2))
    ax_c.figure.canvas.draw()
```
