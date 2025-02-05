# Create Contour Plot

We will now create the contour plot using the `contour()` function. We will pass in the `X`, `Y`, and `Z` data, and set `extend3d=True` to extend the curves vertically into 'ribbons'. We will also set the colormap to `cm.coolwarm` for a nice color scheme.

```python
ax.contour(X, Y, Z, extend3d=True, cmap=cm.coolwarm)
```
