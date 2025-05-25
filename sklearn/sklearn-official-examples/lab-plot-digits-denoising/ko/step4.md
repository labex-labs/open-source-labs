# PCA 기저 학습

선형 PCA 와 커널 PCA 를 모두 사용하여 PCA 기저를 학습합니다. 커널 PCA 는 방사 기저 함수 (RBF) 커널을 사용하여 기저를 학습합니다.

```python
from sklearn.decomposition import PCA, KernelPCA

pca = PCA(n_components=32, random_state=42)
kernel_pca = KernelPCA(
    n_components=400,
    kernel="rbf",
    gamma=1e-3,
    fit_inverse_transform=True,
    alpha=5e-3,
    random_state=42,
)

pca.fit(X_train_noisy)
_ = kernel_pca.fit(X_train_noisy)
```
