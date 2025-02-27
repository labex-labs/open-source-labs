# Sparse components - MiniBatchSparsePCA

Sparse PCA - это модификация метода PCA, которая поощряет разреженность в векторах нагрузки, что позволяет получить более интерпретируемое разложение. Мы используем MiniBatchSparsePCA, которая представляет собой более быструю версию SparsePCA, лучше подходящую для обработки больших наборов данных.

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
