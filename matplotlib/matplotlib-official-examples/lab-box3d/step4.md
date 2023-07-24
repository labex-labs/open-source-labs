# Set Limits of the Plot

Set limits of the plot using the `set` method and passing in the limits of the X, Y, and Z coordinates.

```python
# Set limits of the plot from coord limits
xmin, xmax = X.min(), X.max()
ymin, ymax = Y.min(), Y.max()
zmin, zmax = Z.min(), Z.max()
ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], zlim=[zmin, zmax])
```
