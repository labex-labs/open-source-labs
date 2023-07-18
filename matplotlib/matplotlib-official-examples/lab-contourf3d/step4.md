# Create the Contour Plot

We will now create the contour plot using the `contourf()` method. This method creates filled contours. We will set the `cmap` parameter to `cm.coolwarm` to use the cool-warm color map.

```python
ax.contourf(X, Y, Z, cmap=cm.coolwarm)
```
