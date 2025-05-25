# 추정된 계수 비교

실제 모델, 선형 모델, RANSAC 회귀 분석기의 추정된 계수를 비교합니다.

```python
# 추정된 계수 비교
print("추정된 계수 (실제, 선형 회귀, RANSAC):")
print(coef, lr.coef_, ransac.estimator_.coef_)
```
