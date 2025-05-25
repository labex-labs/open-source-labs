# Embedding Isomap

O Isomap busca um embedding de menor dimensão que mantenha as distâncias geodésicas entre todos os pontos.

```python
isomap = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components, p=1)
S_isomap = isomap.fit_transform(S_points)
```
