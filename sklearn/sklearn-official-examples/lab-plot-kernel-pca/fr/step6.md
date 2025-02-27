# Reprojecter la projection de la PCA Kernel dans l'espace d'origine

Nous allons utiliser la méthode `inverse_transform` de la PCA Kernel pour reprojecter la projection de la PCA Kernel dans l'espace d'origine.

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(kernel_pca.transform(X_test))
```
