# Locally Linear Embeddings

Locally linear embedding (LLE) - это серия локальных анализов главных компонент, которые сравниваются глобально, чтобы найти наилучшую нелинейную встраивание. Мы будем использовать четыре различных метода LLE, то есть Standard, Local tangent space alignment, Hessian eigenmap и Modified locally linear embedding.

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
