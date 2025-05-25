# Componentes Esparsos - MiniBatchSparsePCA

A PCA esparsa é uma variante da PCA que incentiva a esparcidade nos vetores de carregamento, resultando numa decomposição mais interpretável. Usamos o MiniBatchSparsePCA, uma versão mais rápida do SparsePCA, mais adequada para conjuntos de dados grandes.

```python
# Componentes Esparsos - MiniBatchSparsePCA
batch_pca_estimator = decomposition.MiniBatchSparsePCA(
    n_components=n_components, alpha=0.1, max_iter=100, batch_size=3, random_state=rng
)
batch_pca_estimator.fit(faces_centered)
plot_gallery(
    "Componentes Esparsos - MiniBatchSparsePCA",
    batch_pca_estimator.components_[:n_components],
)
```
