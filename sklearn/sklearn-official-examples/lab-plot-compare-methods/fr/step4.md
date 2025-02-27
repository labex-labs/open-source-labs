# Echelle Multidimensionnelle

L'Echelle Multidimensionnelle (Multidimensional Scaling - MDS) cherche une représentation à basse dimension des données dans laquelle les distances respectent bien les distances dans l'espace original à haute dimension.

```python
md_scaling = manifold.MDS(
    n_components=n_components,
    max_iter=50,
    n_init=4,
    random_state=0,
    normalized_stress=False,
)
S_scaling = md_scaling.fit_transform(S_points)
```
