# 将核主成分分析（Kernel PCA）投影反向投影到原始空间

我们将使用核主成分分析（Kernel PCA）的`inverse_transform`方法，将核主成分分析（Kernel PCA）的投影反向投影到原始空间。

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(kernel_pca.transform(X_test))
```
