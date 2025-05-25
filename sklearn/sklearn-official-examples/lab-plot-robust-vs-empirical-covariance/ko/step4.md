# 경험적 공분산 행렬 추정

이 단계에서는 최대 가능도 추정 (MLE) 추정기를 사용하여 데이터 집합의 경험적 공분산 행렬을 추정합니다.

```python
# 데이터 집합의 경험적 공분산 행렬 추정
emp_cov = EmpiricalCovariance().fit(X).covariance_
```
