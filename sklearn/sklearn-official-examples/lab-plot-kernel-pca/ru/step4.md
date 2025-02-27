# Использование Kernel PCA для проекции набора данных

Kernel PCA используется для проекции набора данных на новое пространство, которое сохраняет большую часть его исходной вариации, но также позволяет учитывать нелинейные структуры.

```python
from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
```
