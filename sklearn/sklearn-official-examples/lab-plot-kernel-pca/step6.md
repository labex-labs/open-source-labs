# Back-project the Kernel PCA projection to the original space

We will use the `inverse_transform` method of Kernel PCA to back-project the Kernel PCA projection to the original space.

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(kernel_pca.transform(X_test))
```


