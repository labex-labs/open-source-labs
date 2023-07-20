# Create a Logarithmic Scale Plot

The next type of scale transformation we will explore is logarithmic. To create a logarithmic scale plot, we use the `set_yscale()` method and pass in the string `'log'`. We also add a title and grid to the plot.

```python
# log
plt.plot(x, y)
plt.yscale('log')
plt.title('Logarithmic Scale')
plt.grid(True)
```
