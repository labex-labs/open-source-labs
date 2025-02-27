# Componentes esparsos - MiniBatchSparsePCA

La PCA esparsa es una variante de la PCA que fomenta la esparsidad en los vectores de carga, lo que da como resultado una descomposición más interpretable. Utilizamos MiniBatchSparsePCA, que es una versión más rápida de SparsePCA que es más adecuada para conjuntos de datos grandes.

```python
# Componentes esparsos - MiniBatchSparsePCA
batch_pca_estimator = decomposition.MiniBatchSparsePCA(
    n_components=n_components, alpha=0.1, max_iter=100, batch_size=3, random_state=rng
)
batch_pca_estimator.fit(faces_centered)
plot_gallery(
    "Componentes esparsos - MiniBatchSparsePCA",
    batch_pca_estimator.components_[:n_components],
)
```
