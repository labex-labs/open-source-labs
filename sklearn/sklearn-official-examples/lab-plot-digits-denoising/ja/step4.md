# PCA の基底を学習する

線形 PCA と Kernel PCA の両方を使って PCA の基底を学習します。Kernel PCA は、放射状基底関数（RBF）カーネルを使って基底を学習します。

```python
from sklearn.decomposition import PCA, KernelPCA

pca = PCA(n_components=32, random_state=42)
kernel_pca = KernelPCA(
    n_components=400,
    kernel="rbf",
    gamma=1e-3,
    fit_inverse_transform=True,
    alpha=5e-3,
    random_state=42,
)

pca.fit(X_train_noisy)
_ = kernel_pca.fit(X_train_noisy)
```
