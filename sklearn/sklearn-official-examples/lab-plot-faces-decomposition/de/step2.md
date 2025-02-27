# Eigenfaces - PCA mit randomisierter SVD

Die erste methode, die wir anwenden, ist PCA, eine lineare dimensionsreduzierungstechnik, die die singulärwertzerlegung (SVD) der daten verwendet, um sie in einen raum mit niedrigerer dimension zu projizieren. Wir verwenden eine randomisierte SVD, die eine schnellere annäherung an den standard svd-algorithmus ist. Wir plotten die ersten sechs hauptkomponenten, die als eigenfaces bezeichnet werden.

```python
# Eigenfaces - PCA using randomized SVD
pca_estimator = decomposition.PCA(
    n_components=n_components, svd_solver="randomized", whiten=True
)
pca_estimator.fit(faces_centered)
plot_gallery(
    "Eigenfaces - PCA using randomized SVD", pca_estimator.components_[:n_components]
)
```
