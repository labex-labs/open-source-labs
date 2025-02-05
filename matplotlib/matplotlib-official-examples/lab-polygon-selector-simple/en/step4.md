# Putting It All Together

Let's create a complete example that includes both creating a polygon programmatically and interactively.

```python
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector

# Create a figure and axes
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

# Create a PolygonSelector object and add vertices
selector1 = PolygonSelector(ax1, lambda *args: None)
selector1.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Plot the polygon
ax1.add_patch(plt.Polygon(selector1.verts, alpha=0.3))

# Create another PolygonSelector object for interactive creation
selector2 = PolygonSelector(ax2, lambda *args: None)

print("Click on the figure to create a polygon.")
print("Press the 'esc' key to start a new polygon.")
print("Try holding the 'shift' key to move all of the vertices.")
print("Try holding the 'ctrl' key to move a single vertex.")

plt.show()
```
