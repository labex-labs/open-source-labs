# Spectral Embedding for Non-linear Dimensionality Reduction

This implementation uses Laplacian Eigenmaps, which finds a low dimensional representation of the data using a spectral decomposition of the graph Laplacian.

```python
spectral = manifold.SpectralEmbedding(
    n_components=n_components, n_neighbors=n_neighbors
)
S_spectral = spectral.fit_transform(S_points)
```


