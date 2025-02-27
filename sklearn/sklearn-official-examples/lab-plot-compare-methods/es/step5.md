# Embedding Espectral para Reducción de Dimensionalidad No Lineal

Esta implementación utiliza Mapas Eigen Laplacianos, que encuentra una representación de baja dimensión de los datos utilizando una descomposición espectral del Laplaciano del grafo.

```python
spectral = manifold.SpectralEmbedding(
    n_components=n_components, n_neighbors=n_neighbors
)
S_spectral = spectral.fit_transform(S_points)
```
