# Isomap Embedding

Isomap seeks a lower-dimensional embedding that maintains geodesic distances between all points.

```python
isomap = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components, p=1)
S_isomap = isomap.fit_transform(S_points)
```


