# Eigenfaces - PCA utilizando SVD aleatorizada

El primer método que aplicamos es PCA, que es una técnica de reducción de dimensionalidad lineal que utiliza la Descomposición en Valores Singulares (SVD) de los datos para proyectarlos a un espacio de dimensión más baja. Utilizamos SVD aleatorizada, que es una aproximación más rápida del algoritmo de SVD estándar. Representamos los primeros seis componentes principales, que se denominan eigenfaces.

```python
# Eigenfaces - PCA utilizando SVD aleatorizada
pca_estimator = decomposition.PCA(
    n_components=n_components, svd_solver="randomized", whiten=True
)
pca_estimator.fit(faces_centered)
plot_gallery(
    "Eigenfaces - PCA using randomized SVD", pca_estimator.components_[:n_components]
)
```
