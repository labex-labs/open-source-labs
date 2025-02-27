# Realizar MDS no métrico

También realizaremos MDS no métrico en el mismo conjunto de datos para comparación. Utilizaremos las mismas opciones que MDS, excepto que estableceremos la opción métrica en False.

```python
nmds = manifold.MDS(
    n_components=2,
    metric=False,
    max_iter=3000,
    eps=1e-12,
    dissimilarity="precomputed",
    random_state=seed,
    n_jobs=1,
    n_init=1,
    normalized_stress="auto",
)
npos = nmds.fit_transform(similarities, init=pos)
```
