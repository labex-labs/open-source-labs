# Define the initialization function

We need to define an initialization function that will set the initial state of the plot. In this function, we will set the y-axis limits and clear the data from the line object.

```python
def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,
```
