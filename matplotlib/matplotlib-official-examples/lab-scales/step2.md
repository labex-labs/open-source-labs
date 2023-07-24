# Create a Linear Scale Plot

The first type of scale transformation we will explore is linear. This is the default scale used in Matplotlib. To create a linear scale plot, we use the `set_yscale()` method and pass in the string `'linear'`. We also add a title and grid to the plot.

```python
# linear
plt.plot(x, y)
plt.yscale('linear')
plt.title('Linear Scale')
plt.grid(True)
```
