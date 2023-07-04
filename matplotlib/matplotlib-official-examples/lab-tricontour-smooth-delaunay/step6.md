# Improve Triangulation

We use a `TriAnalyzer` to improve the triangulation by removing badly shaped (flat) triangles from the border of the triangulation. We then apply the mask to the triangulation using `set_mask`.

```python
# masking badly shaped triangles at the border of the triangular mesh.
mask = TriAnalyzer(tri).get_flat_tri_mask(min_circle_ratio)
tri.set_mask(mask)
```
