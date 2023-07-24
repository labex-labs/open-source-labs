# Project contour profiles onto the walls of the graph

In this step, we will project contour profiles onto the walls of the graph by plotting the contours for each dimension with appropriate offsets.

```python
# Plot projections of the contours for each dimension
ax.contour(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contour(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
