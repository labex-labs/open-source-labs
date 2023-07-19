# Create Data

Next, we need to create the data that we will use to plot the lines. We will use `numpy` to create a 2D array of `x` and `y` values.

```python
x = np.arange(100)
ys = x[:50, np.newaxis] + x[np.newaxis, :]
```
