# Lokale lineare Einbettungen

Lokale lineare Einbettung (LLE) ist eine Reihe lokaler Hauptkomponentenanalysen, die global verglichen werden, um die beste nichtlineare Einbettung zu finden. Wir werden vier verschiedene Methoden der LLE verwenden, nämlich Standard, Lokale Tangentialraumausrichtung, Hessische Eigenkarte und Modifizierte lokale lineare Einbettung.

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
