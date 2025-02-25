# Triangulation verbessern

Wir verwenden einen `TriAnalyzer`, um die Triangulation zu verbessern, indem wir schlecht geformte (flache) Dreiecke von der Grenze der Triangulation entfernen. Anschließend wenden wir die Maske auf die Triangulation an, indem wir `set_mask` verwenden.

```python
# masking badly shaped triangles at the border of the triangular mesh.
mask = TriAnalyzer(tri).get_flat_tri_mask(min_circle_ratio)
tri.set_mask(mask)
```
