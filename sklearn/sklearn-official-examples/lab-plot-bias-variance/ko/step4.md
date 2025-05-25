# 비교할 모델 정의

비교할 두 가지 모델을 정의합니다: 단일 의사결정 트리와 의사결정 트리의 배깅 앙상블입니다.

```python
estimators = [
    ("Tree", DecisionTreeRegressor()),
    ("Bagging(Tree)", BaggingRegressor(DecisionTreeRegressor())),
]
n_estimators = len(estimators)
```
