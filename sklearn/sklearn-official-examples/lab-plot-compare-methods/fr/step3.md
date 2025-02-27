# Embeding Isomap

Isomap cherche un emmbeding à basse dimension qui conserve les distances géodésiques entre tous les points.

```python
isomap = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components, p=1)
S_isomap = isomap.fit_transform(S_points)
```
