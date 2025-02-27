# Обратная проекция Kernel PCA на исходное пространство

Мы будем использовать метод `inverse_transform` Kernel PCA для обратной проекции Kernel PCA на исходное пространство.

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(kernel_pca.transform(X_test))
```
