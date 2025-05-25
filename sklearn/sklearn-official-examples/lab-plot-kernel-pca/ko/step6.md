# 커널 PCA 투영을 원래 공간으로 되돌리기

커널 PCA 투영을 원래 공간으로 되돌리기 위해 커널 PCA 의 `inverse_transform` 메서드를 사용합니다.

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(kernel_pca.transform(X_test))
```
