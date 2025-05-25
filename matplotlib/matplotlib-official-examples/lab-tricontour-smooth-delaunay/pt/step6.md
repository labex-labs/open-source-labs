# Melhorar a Triangulação

Usamos um `TriAnalyzer` para melhorar a triangulação, removendo triângulos mal formados (planos) da borda da triangulação. Em seguida, aplicamos a máscara à triangulação usando `set_mask`.

```python
# masking badly shaped triangles at the border of the triangular mesh.
mask = TriAnalyzer(tri).get_flat_tri_mask(min_circle_ratio)
tri.set_mask(mask)
```
