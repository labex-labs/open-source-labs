# Kernel PCA の射影を元の空間に逆射影する

Kernel PCA の射影を元の空間に逆射影するために、Kernel PCA の `inverse_transform` メソッドを使用します。

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(kernel_pca.transform(X_test))
```
