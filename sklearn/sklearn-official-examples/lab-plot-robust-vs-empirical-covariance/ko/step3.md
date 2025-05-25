# 강력한 공분산 행렬 추정

이 단계에서는 최소 공분산 행렬 결정 (MCD) 추정기를 사용하여 데이터 집합의 강력한 공분산 행렬을 추정합니다.

```python
# 데이터 집합의 강력한 공분산 행렬 추정
mcd = MinCovDet().fit(X)
robust_cov = mcd.covariance_
```
