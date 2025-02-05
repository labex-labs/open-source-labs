# Create a Logit Scale Plot

The fourth type of scale transformation we will explore is logit. This type of scale is useful when dealing with data that is bounded by 0 and 1. To create a logit scale plot, we use the `set_yscale()` method and pass in the string `'logit'`. We also add a title and grid to the plot.

```python
# logit
plt.plot(x, y)
plt.yscale('logit')
plt.title('Logit Scale')
plt.grid(True)
```
