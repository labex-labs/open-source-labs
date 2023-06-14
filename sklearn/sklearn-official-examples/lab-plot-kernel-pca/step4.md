# Use Kernel PCA to project the dataset

Kernel PCA is used to project the dataset onto a new space that preserves most of its original variation, but also allows for non-linear structures.

```python
from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
```


