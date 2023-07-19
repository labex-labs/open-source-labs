# Gouraud Shading

`Gouraud shading` can also be specified, where the color in the quadrilaterals is linearly interpolated between the grid points. The shapes of `X`, `Y`, `Z` must be the same. We can visualize the grid using the following code block:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='gouraud', cmap='viridis')
ax.set_title('Gouraud Shading')
plt.show()
```
