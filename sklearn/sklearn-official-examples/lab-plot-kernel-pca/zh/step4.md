# 使用核主成分分析（Kernel PCA）对数据集进行投影

核主成分分析（Kernel PCA）用于将数据集投影到一个新的空间，该空间不仅保留了其大部分原始变化，还能处理非线性结构。

```python
from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
```
