# 의사결정 트리 모델 학습

이 단계에서는 원본 데이터셋에 의사결정 트리 모델을 학습시킵니다.

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X, y)
```
