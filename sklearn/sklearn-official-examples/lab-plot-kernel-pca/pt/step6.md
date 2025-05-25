# Projetar novamente a projeção PCA Kernel para o espaço original

Usaremos o método `inverse_transform` da PCA Kernel para projetar novamente a projeção PCA Kernel para o espaço original.

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(kernel_pca.transform(X_test))
```
