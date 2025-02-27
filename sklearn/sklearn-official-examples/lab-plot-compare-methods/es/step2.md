# Embedding Lineal Local

El Embedding Lineal Local (LLE) es una serie de Análisis de Componentes Principales locales que se comparan globalmente para encontrar la mejor incrustación no lineal. Utilizaremos cuatro métodos diferentes de LLE, es decir, Estandar, Alineación del espacio tangente local, Mapa eigen Hessiano y Embedding Lineal Local Modificado.

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
