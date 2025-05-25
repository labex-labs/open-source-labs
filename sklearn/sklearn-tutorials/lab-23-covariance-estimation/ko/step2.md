# 축소된 공분산

최대 가능도 추정량은 편향되지 않았지만, 공분산 행렬의 고유값을 정확하게 추정하지 못할 수 있으며, 이로 인해 결과가 부정확해질 수 있습니다. 이 문제를 완화하기 위해 축소 (shrinkage) 라는 기술이 사용됩니다. 축소는 경험적 공분산 행렬의 가장 작은 고유값과 가장 큰 고유값의 비율을 줄여 추정의 정확도를 향상시킵니다. `sklearn.covariance` 패키지는 데이터에 축소된 추정량을 맞출 수 있는 `ShrunkCovariance` 클래스를 제공합니다.

```python
from sklearn.covariance import ShrunkCovariance

# ShrunkCovariance 객체를 생성하고 데이터에 맞춥니다.
shrunk_estimator = ShrunkCovariance().fit(data)

# 축소된 공분산 행렬을 계산합니다.
shrunk_covariance_matrix = shrunk_estimator.covariance_
```
