# Embedding Isomap

Isomap busca una incrustación de menor dimensión que mantenga las distancias geodésicas entre todos los puntos.

```python
isomap = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components, p=1)
S_isomap = isomap.fit_transform(S_points)
```
