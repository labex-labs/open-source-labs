# Eigenfaces - PCA using randomized SVD

The first method we apply is PCA, which is a linear dimensionality reduction technique that uses Singular Value Decomposition (SVD) of the data to project it to a lower dimensional space. We use randomized SVD, which is a faster approximation of the standard SVD algorithm. We plot the first six principal components, which are called eigenfaces.

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
