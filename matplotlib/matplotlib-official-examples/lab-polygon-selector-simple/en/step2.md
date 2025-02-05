# Create a Polygon Programmatically

To create a polygon programmatically, we need to create a `Figure` object and an `Axes` object. Then, we can create a `PolygonSelector` object and add vertices to it. Finally, we can plot the polygon on the `Axes`.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

# Add three vertices
selector.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Plot the polygon
ax.add_patch(plt.Polygon(selector.verts, alpha=0.3))
plt.show()
```
