# Isomap-Einbettung

Isomap sucht eine Einbettung in einer niedrigeren Dimension, die die geodätischen Distanzen zwischen allen Punkten beibehält.

```python
isomap = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components, p=1)
S_isomap = isomap.fit_transform(S_points)
```
