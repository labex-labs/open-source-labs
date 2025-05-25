# 커널 함수 정의

다음으로 커널 함수를 정의합니다. 이 예제에서는 Radial Basis Function(RBF) 커널을 사용합니다. 등방성 버전과 이방성 버전의 두 가지 RBF 커널 버전을 정의합니다.

```python
kernel = 1.0 * RBF([1.0])
gpc_rbf_isotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)

kernel = 1.0 * RBF([1.0, 1.0])
gpc_rbf_anisotropic = GaussianProcessClassifier(kernel=kernel).fit(X, y)
```
