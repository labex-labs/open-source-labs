# Generate Data

Next, we need to generate some data to plot. In this example, we will create three arrays: one for the x-axis values, one for the y-axis values in the first plot, and one for the y-axis values in the third plot.

```python
dt = 0.01
x = np.arange(-50.0, 50.0, dt)
y1 = np.arange(0, 100.0, dt)
y3 = np.sin(x / 3.0)
```
