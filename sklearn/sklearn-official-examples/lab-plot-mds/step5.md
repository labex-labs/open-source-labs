# Perform Non-Metric MDS

We will also perform non-metric MDS on the same dataset for comparison. We will use the same options as MDS, except we will set the metric option to False.

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


