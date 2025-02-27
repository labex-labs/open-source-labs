# Utiliser la PCA Kernel pour projeter l'ensemble de données

La PCA Kernel est utilisée pour projeter l'ensemble de données dans un nouvel espace qui conserve la majeure partie de sa variation initiale, mais permet également des structures non linéaires.

```python
from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
```
