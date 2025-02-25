# Améliorer la triangulation

Nous utilisons un `TriAnalyzer` pour améliorer la triangulation en éliminant les triangles mal formés (plats) sur la bordure de la triangulation. Nous appliquons ensuite le masque à la triangulation en utilisant `set_mask`.

```python
# masquage des triangles mal formés à la bordure du maillage triangulaire.
mask = TriAnalyzer(tri).get_flat_tri_mask(min_circle_ratio)
tri.set_mask(mask)
```
