# Sparse Komponenten - MiniBatchSparsePCA

Sparse PCA ist eine Variante von PCA, die Sparsamkeit in den Ladevektoren fördert, was zu einer interpretierbareren Dekomposition führt. Wir verwenden MiniBatchSparsePCA, eine schnellere Version von SparsePCA, die für große Datensätze besser geeignet ist.

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
