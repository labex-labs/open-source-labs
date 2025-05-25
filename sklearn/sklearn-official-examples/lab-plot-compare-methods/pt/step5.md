# Embedding Espectral para Redução de Dimensionalidade Não Linear

Esta implementação utiliza o método de _Laplacian Eigenmaps_, que encontra uma representação de baixa dimensão dos dados utilizando uma decomposição espectral do Laplaciano do grafo.

```python
spectral = manifold.SpectralEmbedding(
    n_components=n_components, n_neighbors=n_neighbors
)
S_spectral = spectral.fit_transform(S_points)
```
