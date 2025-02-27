# Isomap Embedding

Isomap ищет встраивание в более низкой размерности, которое сохраняет геодезические расстояния между всеми точками.

```python
isomap = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components, p=1)
S_isomap = isomap.fit_transform(S_points)
```
