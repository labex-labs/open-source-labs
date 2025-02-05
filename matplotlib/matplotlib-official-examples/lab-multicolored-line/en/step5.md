# Create a Colorbar

We will create a colorbar to show the mapping between colors and `dydx` values. We will use the `colorbar` function from `matplotlib.pyplot` to create a colorbar.

```python
line = plt.gca().add_collection(lc)
plt.colorbar(line)
```
