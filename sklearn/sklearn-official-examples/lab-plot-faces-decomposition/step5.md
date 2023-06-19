# Sparse components - MiniBatchSparsePCA

Sparse PCA is a variant of PCA that encourages sparsity in the loading vectors, resulting in a more interpretable decomposition. We use MiniBatchSparsePCA, which is a faster version of SparsePCA that is better suited for large datasets.

```python
# Sparse components - MiniBatchSparsePCA
batch_pca_estimator = decomposition.MiniBatchSparsePCA(
    n_components=n_components, alpha=0.1, max_iter=100, batch_size=3, random_state=rng
)
batch_pca_estimator.fit(faces_centered)
plot_gallery(
    "Sparse components - MiniBatchSparsePCA",
    batch_pca_estimator.components_[:n_components],
)
```


