# MCD 및 MLE 공분산 추정기를 데이터에 적용

MCD 및 MLE 기반 공분산 추정기를 데이터에 적용하고 추정된 공분산 행렬을 출력합니다. MLE 기반 추정기의 특징 2 의 추정된 분산 (7.5) 은 MCD 강력 추정기 (1.2) 보다 훨씬 높습니다. 이는 MCD 기반 강력 추정기가 특징 2 에서 훨씬 큰 분산을 갖도록 설계된 이상치 샘플에 훨씬 더 강건하다는 것을 보여줍니다.

```python
from sklearn.covariance import EmpiricalCovariance, MinCovDet

# 데이터에 MCD 강력 추정기를 적용
robust_cov = MinCovDet().fit(X)
# 데이터에 MLE 추정기를 적용
emp_cov = EmpiricalCovariance().fit(X)
print(
    "추정된 공분산 행렬:\nMCD (강력):\n{}\nMLE:\n{}".format(
        robust_cov.covariance_, emp_cov.covariance_
    )
)
```
