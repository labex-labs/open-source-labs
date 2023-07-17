# Create a Figure and Connect the Close Event

In this step, we will create a figure and connect the close event to the `on_close` function defined in Step 1. This is done using the `mpl_connect` method of the figure's canvas.

```python
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close)
```
