# 테스트 데이터에서 가능도 계산

`sklearn.covariance` 모듈의 `ShrunkCovariance` 클래스와 `scipy.linalg` 모듈의 `log_likelihood` 함수를 사용하여 테스트 데이터에서 음의 로그 가능도를 계산합니다. 가능한 축소 계수 값의 범위를 설정하고 각 값에 대한 가능도를 계산합니다.

```python
from sklearn.covariance import ShrunkCovariance, empirical_covariance, log_likelihood
from scipy import linalg

shrinkages = np.logspace(-2, 0, 30)
negative_logliks = [
    -ShrunkCovariance(shrinkage=s).fit(X_train).score(X_test) for s in shrinkages
]

real_cov = np.dot(coloring_matrix.T, coloring_matrix)
emp_cov = empirical_covariance(X_train)
loglik_real = -log_likelihood(emp_cov, linalg.inv(real_cov))
```
