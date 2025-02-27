# Verwende die Kernel PCA, um den Datensatz zu projizieren

Die Kernel PCA wird verwendet, um den Datensatz in einen neuen Raum zu projizieren, in dem die meiste ursprüngliche Variation erhalten bleibt, aber auch nicht-lineare Strukturen ermöglicht.

```python
from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
```
