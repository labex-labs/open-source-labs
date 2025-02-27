# Lerne die PCA-Basis

Wir lernen die PCA-Basis sowohl mit linearer PCA als auch mit Kernel PCA. Kernel PCA verwendet den radial basis function (RBF)-Kernel, um die Basis zu lernen.

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
