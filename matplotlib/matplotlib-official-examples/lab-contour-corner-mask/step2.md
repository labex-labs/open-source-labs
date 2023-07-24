# Creating Data for Plotting

In this step, we will create data to plot on a contour plot. We use the `np.meshgrid()` function to create a grid of points, and then calculate the `z` values using the sine and cosine functions.

```python
# Data to plot.
x, y = np.meshgrid(np.arange(7), np.arange(10))
z = np.sin(0.5 * x) * np.cos(0.52 * y)
```
