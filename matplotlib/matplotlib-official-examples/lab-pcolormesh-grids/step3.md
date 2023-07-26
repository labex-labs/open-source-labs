# Flat Shading

The `pcolormesh` function in Matplotlib can visualize 2D grids. The grid specification with the least assumptions is `shading='flat'` and if the grid is one larger than the data in each dimension, i.e., has shape `(M+1, N+1)`. In that case, `X` and `Y` specify the corners of quadrilaterals that are colored with the values in `Z`. We can visualize the grid using the following code block:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='flat', cmap='viridis')
ax.set_title('Flat Shading')
plt.show()
```
