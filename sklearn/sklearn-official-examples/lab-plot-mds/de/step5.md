# Nicht-metrische Multi-dimensionale Skalierung (Non-Metric MDS) durchführen

Wir werden auch nicht-metrische MDS auf dem gleichen Datensatz durchführen, um einen Vergleich durchzuführen. Wir werden die gleichen Optionen wie bei MDS verwenden, nur dass wir die Option „metric“ auf False setzen.

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
