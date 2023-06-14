# Perform MDS

We will then perform MDS on the noisy dataset using scikit-learn's MDS class. We will use the precomputed dissimilarity option since we have already calculated the pairwise distances between the data points. We will also set the number of components to 2 for 2D visualization.

```python
mds = manifold.MDS(
    n_components=2,
    max_iter=3000,
    eps=1e-9,
    random_state=seed,
    dissimilarity="precomputed",
    n_jobs=1,
    normalized_stress="auto",
)
pos = mds.fit(similarities).embedding_
```


