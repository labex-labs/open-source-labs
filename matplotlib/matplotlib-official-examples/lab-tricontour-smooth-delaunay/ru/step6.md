# Улучшить триангуляцию

Мы используем `TriAnalyzer`, чтобы улучшить триангуляцию, удаляя плохо сформированные (плоские) треугольники из границы триангуляции. Затем мы применяем маску к триангуляции с использованием `set_mask`.

```python
# masking badly shaped triangles at the border of the triangular mesh.
mask = TriAnalyzer(tri).get_flat_tri_mask(min_circle_ratio)
tri.set_mask(mask)
```
