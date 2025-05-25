# Ledoit-Wolf 축소

Ledoit-Wolf 축소 방법은 추정된 공분산 행렬과 실제 공분산 행렬 사이의 평균 제곱 오차를 최소화하는 최적의 축소 계수를 제공합니다. `sklearn.covariance` 패키지에는 주어진 데이터 집합에 대한 Ledoit-Wolf 추정량을 계산하는 데 사용할 수 있는 `ledoit_wolf` 함수가 포함되어 있습니다.

```python
from sklearn.covariance import ledoit_wolf

# 공분산 행렬의 Ledoit-Wolf 추정량을 계산합니다.
ledoit_wolf_covariance_matrix = ledoit_wolf(data)[0]
```
