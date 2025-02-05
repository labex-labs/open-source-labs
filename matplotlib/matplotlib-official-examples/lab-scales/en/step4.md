# Create a Symmetrical Logarithmic Scale Plot

The third type of scale transformation we will explore is symmetrical logarithmic. This type of scale is useful when dealing with data that contains both positive and negative values. To create a symmetrical logarithmic scale plot, we use the `set_yscale()` method and pass in the string `'symlog'`. We also set the `linthresh` parameter to `0.02` to specify the range of values around zero that will be linearly scaled. We also add a title and grid to the plot.

```python
# symmetric log
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthresh=0.02)
plt.title('Symmetrical Logarithmic Scale')
plt.grid(True)
```
