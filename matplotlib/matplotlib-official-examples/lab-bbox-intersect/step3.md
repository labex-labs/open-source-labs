# Generate random lines

We will generate 12 random lines using `numpy` library and plot them using `plot` method. If a line intersects the rectangle, its color will be red, otherwise blue. We will use `Path` class to create a line and `intersects_bbox` method to check if it intersects the rectangle.

```python
bbox = Bbox.from_bounds(left, bottom, width, height)

for i in range(12):
    vertices = (np.random.random((2, 2)) - 0.5) * 6.0
    path = Path(vertices)
    if path.intersects_bbox(bbox):
        color = 'r'
    else:
        color = 'b'
    ax.plot(vertices[:, 0], vertices[:, 1], color=color)
```
