# Projektieren Sie die Kernel-PCA-Projektion zurück in den ursprünglichen Raum

Wir werden die `inverse_transform`-Methode der Kernel PCA verwenden, um die Kernel-PCA-Projektion zurück in den ursprünglichen Raum zu projizieren.

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(kernel_pca.transform(X_test))
```
