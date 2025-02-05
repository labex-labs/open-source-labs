# Flat Shading, Same Shape Grid

If the grid is the same shape as the data in each dimension, we cannot use `shading='flat'`. Historically, Matplotlib silently dropped the last row and column of `Z` in this case, to match Matlab's behavior. If this behavior is still desired, simply drop the last row and column manually. We can visualize the grid using the following code block:

```python
fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z[:-1, :-1], shading='flat', cmap='viridis')
ax.set_title('Flat Shading, Same Shape Grid')
plt.show()
```
