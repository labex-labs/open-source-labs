# Create polygons

We create polygons using `Polygon()` and append them to the list of patches.

```python
for i in range(N):
    polygon = Polygon(np.random.rand(N, 2), closed=True)
    patches.append(polygon)
```
