# Proyectar de vuelta la proyección de PCA Kernel al espacio original

Usaremos el método `inverse_transform` de PCA Kernel para proyectar de vuelta la proyección de PCA Kernel al espacio original.

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(kernel_pca.transform(X_test))
```
