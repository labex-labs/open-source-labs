# Create a Polygon Interactively

To create a polygon interactively, we need to create a `Figure` object and an `Axes` object. Then, we can create a `PolygonSelector` object and add vertices to it by clicking on the plot. We can also use the `shift` and `ctrl` keys to move the vertices.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

print("Click on the figure to create a polygon.")
print("Press the 'esc' key to start a new polygon.")
print("Try holding the 'shift' key to move all of the vertices.")
print("Try holding the 'ctrl' key to move a single vertex.")

plt.show()
```
