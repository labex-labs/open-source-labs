# Spektrale Einbettung zur nichtlinearen Dimensionsreduzierung

Diese Implementierung verwendet Laplace-Eigenkarten, die eine Darstellung der Daten in einer niedrigen Dimension mithilfe einer spektralen Zerlegung der Graphen-Laplace-Operator findet.

```python
spectral = manifold.SpectralEmbedding(
    n_components=n_components, n_neighbors=n_neighbors
)
S_spectral = spectral.fit_transform(S_points)
```
