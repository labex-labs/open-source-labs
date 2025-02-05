# Project Contour Profiles

We will now project the contour profiles onto the walls of the graph. This is done using the `contourf` method. We will set the `zdir` parameter to 'z', 'x', and 'y' to project the contour profiles onto the z, x, and y walls respectively. We will also set the `offset` parameter to match the appropriate axes limits.

```python
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
