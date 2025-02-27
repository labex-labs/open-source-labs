# Effectuer l'analyse en composantes principales multi-dimensionnelles non métrique (Non-Metric MDS)

Nous allons également effectuer l'analyse en composantes principales multi-dimensionnelles non métrique sur le même ensemble de données pour la comparaison. Nous utiliserons les mêmes options que pour l'analyse en composantes principales multi-dimensionnelles, sauf que nous définirons l'option métrique sur False.

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
