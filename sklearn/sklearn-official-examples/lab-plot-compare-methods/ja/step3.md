# Isomap 埋め込み

Isomap は、すべての点間の測地距離を維持する低次元埋め込みを求めます。

```python
isomap = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components, p=1)
S_isomap = isomap.fit_transform(S_points)
```
