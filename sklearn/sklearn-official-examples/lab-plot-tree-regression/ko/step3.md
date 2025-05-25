# 회귀 모델 학습

두 가지 다른 최대 깊이 (2 와 5) 를 사용하여 회귀 모델을 학습합니다.

```python
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, y)
regr_2.fit(X, y)
```
