# Usar PCA Kernel para projetar o conjunto de dados

A PCA Kernel é usada para projetar o conjunto de dados em um novo espaço que preserva a maior parte de sua variação original, mas também permite estruturas não lineares.

```python
from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
```
