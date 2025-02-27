# Embedding Spectral pour la réduction de dimension non linéaire

Cette implémentation utilise les Cartes d'eigenvaleur de Laplacien, qui trouve une représentation à basse dimension des données en utilisant une décomposition spectrale du Laplacien du graphe.

```python
spectral = manifold.SpectralEmbedding(
    n_components=n_components, n_neighbors=n_neighbors
)
S_spectral = spectral.fit_transform(S_points)
```
