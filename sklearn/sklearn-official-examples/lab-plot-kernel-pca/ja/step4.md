# Kernel PCA を使ってデータセットを射影する

Kernel PCA は、データセットの元の変動の大部分を保つだけでなく、非線形構造も許容する新しい空間にデータセットを射影するために使用されます。

```python
from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
```
