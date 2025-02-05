# Create a Continuous Norm

We will create a continuous norm to map from data points to colors. We will use the `Normalize` function from `matplotlib.pyplot` to normalize the `dydx` values between its minimum and maximum. We will then use the `LineCollection` function to create a set of line segments and color them individually based on their derivative. We will use the `set_array` function to set the values used for colormapping.

```python
norm = plt.Normalize(dydx.min(), dydx.max())
lc = LineCollection(segments, cmap='viridis', norm=norm)
lc.set_array(dydx)
lc.set_linewidth(2)
```
