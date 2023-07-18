# Create the Quiver Plot

With the grid and direction of the arrows defined, we can create the quiver plot. In this example, we will use Matplotlib's `quiver` function to create the plot. The `length` parameter sets the length of the arrows and the `normalize` parameter normalizes the arrows to a length of 1.

```python
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
```
