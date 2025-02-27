# Apprendre la base PCA

Nous apprenons la base PCA à l'aide de la PCA linéaire et de la PCA Kernel. La PCA Kernel utilise le noyau de fonction de base radiale (RBF) pour apprendre la base.

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
