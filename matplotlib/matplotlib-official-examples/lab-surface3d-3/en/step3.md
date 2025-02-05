# Create colors for the surface plot

In this step, we will create colors for the surface plot. We will create an empty array of strings with the same shape as the meshgrid, and populate it with two colors in a checkerboard pattern.

```python
# Create colors for the surface plot
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
```
