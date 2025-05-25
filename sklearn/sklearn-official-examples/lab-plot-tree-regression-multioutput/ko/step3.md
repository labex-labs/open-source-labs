# 회귀 모델 학습

이 단계에서는 회귀 모델을 학습합니다. `sklearn.tree`의 `DecisionTreeRegressor`를 사용하여 서로 다른 최대 깊이를 가진 세 가지 다른 모델을 학습합니다.

```python
# 회귀 모델 학습
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_3 = DecisionTreeRegressor(max_depth=8)
regr_1.fit(X, y)
regr_2.fit(X, y)
regr_3.fit(X, y)
```
