# 경험적 공분산

경험적 공분산 행렬은 데이터 집합의 공분산 행렬을 추정하는 데 일반적으로 사용되는 방법입니다. 최대 가능도 추정의 원리를 기반으로 하며 관측치가 독립적이고 동일한 분포 (i.i.d.) 를 따른다고 가정합니다. `sklearn.covariance` 패키지의 `empirical_covariance` 함수를 사용하여 주어진 데이터 집합의 경험적 공분산 행렬을 계산할 수 있습니다.

```python
from sklearn.covariance import empirical_covariance

# 경험적 공분산 행렬 계산
covariance_matrix = empirical_covariance(data)
```
