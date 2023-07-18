# Create a Function to Set Default Parameters

To create a function that sets the default parameters for your figures, you can use the `rcParams.update()` method. This method takes a dictionary of parameter names and values, and updates the current default values with the new ones. Here's an example of a function that sets some default parameters for publication figures:

```python
def set_pub():
    rcParams.update({
        "font.weight": "bold",  # bold fonts
        "tick.labelsize": 15,   # large tick labels
        "lines.linewidth": 1,   # thick lines
        "lines.color": "k",     # black lines
        "grid.color": "0.5",    # gray gridlines
        "grid.linestyle": "-",  # solid gridlines
        "grid.linewidth": 0.5,  # thin gridlines
        "savefig.dpi": 300,     # higher resolution output.
    })
```
