# Spectral Embedding for Non-linear Dimensionality Reduction

Данная реализация использует Laplacian Eigenmaps, которая находит низкоразмерное представление данных с использованием спектрального разложения графа Лапласиана.

```python
spectral = manifold.SpectralEmbedding(
    n_components=n_components, n_neighbors=n_neighbors
)
S_spectral = spectral.fit_transform(S_points)
```
