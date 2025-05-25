# Eigenfaces - PCA usando SVD aleatorizado

O primeiro método que aplicamos é a PCA, que é uma técnica de redução de dimensionalidade linear que utiliza a Decomposição em Valores Singulares (SVD) dos dados para projetá-los em um espaço de menor dimensão. Usamos SVD aleatorizado, que é uma aproximação mais rápida do algoritmo SVD padrão. Plotamos os seis primeiros componentes principais, que são chamados de eigenfaces.

```python
# Eigenfaces - PCA usando SVD aleatorizado
pca_estimator = decomposition.PCA(
    n_components=n_components, svd_solver="randomized", whiten=True
)
pca_estimator.fit(faces_centered)
plot_gallery(
    "Eigenfaces - PCA usando SVD aleatorizado", pca_estimator.components_[:n_components]
)
```
