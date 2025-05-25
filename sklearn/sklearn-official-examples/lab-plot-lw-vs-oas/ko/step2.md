# 데이터 생성

다음으로, AR(1) 과정을 따르는 공분산 행렬을 가진 가우시안 분포 데이터를 생성합니다. `scipy.linalg`의 `toeplitz`와 `cholesky` 함수를 사용하여 공분산 행렬을 생성합니다.

```python
np.random.seed(0)

n_features = 100
r = 0.1
real_cov = toeplitz(r ** np.arange(n_features))
coloring_matrix = cholesky(real_cov)
```
