# Composantes sparses - MiniBatchSparsePCA

La PCA sparse est une variante de la PCA qui encourage la sparsité dans les vecteurs de chargement, ce qui conduit à une décomposition plus interprétable. Nous utilisons MiniBatchSparsePCA, qui est une version plus rapide de SparsePCA qui est mieux adaptée aux grands jeux de données.

```python
# Composantes sparses - MiniBatchSparsePCA
batch_pca_estimator = decomposition.MiniBatchSparsePCA(
    n_components=n_components, alpha=0.1, max_iter=100, batch_size=3, random_state=rng
)
batch_pca_estimator.fit(faces_centered)
plot_gallery(
    "Composantes sparses - MiniBatchSparsePCA",
    batch_pca_estimator.components_[:n_components],
)
```
