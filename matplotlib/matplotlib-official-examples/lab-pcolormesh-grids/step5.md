# Nearest Shading, Same Shape Grid

Usually, dropping a row and column of data is not what the user means when they make `X`, `Y`, and `Z` all the same shape. For this case, Matplotlib allows `shading='nearest'` and centers the colored quadrilaterals on the grid points. If a grid that is not the correct shape is passed with `shading='nearest'`, an error is raised. We can visualize the grid using the following code block:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='nearest', cmap='viridis')
ax.set_title('Nearest Shading, Same Shape Grid')
plt.show()
```
