# Embeddings Linéaires Locaux

L'Embedding Linéaire Local (Locally Linear Embedding - LLE) est une série d'Analyses en Composantes Principales locales qui sont comparées globalement pour trouver la meilleure non-linéaire embedding. Nous utiliserons quatre méthodes différentes de LLE, soit la Standard, l'Ajustement de l'espace tangent local, la Carte d'eigenvaleur de Hessian et l'Embedding Linéaire Local Modifié.

```python
params = {
    "n_neighbors": n_neighbors,
    "n_components": n_components,
    "eigen_solver": "auto",
    "random_state": 0,
}

lle_standard = manifold.LocallyLinearEmbedding(method="standard", **params)
S_standard = lle_standard.fit_transform(S_points)

lle_ltsa = manifold.LocallyLinearEmbedding(method="ltsa", **params)
S_ltsa = lle_ltsa.fit_transform(S_points)

lle_hessian = manifold.LocallyLinearEmbedding(method="hessian", **params)
S_hessian = lle_hessian.fit_transform(S_points)

lle_mod = manifold.LocallyLinearEmbedding(method="modified", **params)
S_mod = lle_mod.fit_transform(S_points)
```
