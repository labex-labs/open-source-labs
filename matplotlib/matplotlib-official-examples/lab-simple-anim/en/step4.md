# Define the Animation Function

The animation function will be called by the `FuncAnimation()` function and will be used to update the plot with new data. In this example, we will be updating the y-axis values of the line plot with a sine wave that has a changing amplitude over time.

```python
def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,
```
