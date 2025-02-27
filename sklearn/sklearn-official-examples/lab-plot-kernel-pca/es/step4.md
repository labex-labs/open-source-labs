# Usar PCA Kernel para proyectar el conjunto de datos

El PCA Kernel se utiliza para proyectar el conjunto de datos en un nuevo espacio que conserva la mayor parte de su variación original, pero también permite estructuras no lineales.

```python
from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
```
