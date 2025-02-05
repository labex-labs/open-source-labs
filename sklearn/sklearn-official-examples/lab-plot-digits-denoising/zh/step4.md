# 学习主成分分析（PCA）基

我们使用线性主成分分析（PCA）和核主成分分析（Kernel PCA）来学习主成分分析基。核主成分分析使用径向基函数（RBF）核来学习基。

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
