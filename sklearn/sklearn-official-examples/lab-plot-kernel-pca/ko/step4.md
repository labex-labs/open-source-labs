# 커널 PCA 를 이용한 데이터셋 투영

커널 PCA 는 데이터셋을 원래의 변동성을 대부분 유지하면서도 비선형 구조를 반영할 수 있는 새로운 공간으로 투영하는 데 사용됩니다.

```python
from sklearn.decomposition import KernelPCA

kernel_pca = KernelPCA(
    n_components=None, kernel="rbf", gamma=10, fit_inverse_transform=True, alpha=0.1
)

X_test_kernel_pca = kernel_pca.fit(X_train).transform(X_test)
```
