# 等距映射嵌入

等距映射（Isomap）旨在寻找一种低维嵌入，该嵌入能保持所有点之间的测地距离。

```python
isomap = manifold.Isomap(n_neighbors=n_neighbors, n_components=n_components, p=1)
S_isomap = isomap.fit_transform(S_points)
```
