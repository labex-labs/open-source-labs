# 결정 경계 시각화

Scikit-learn 의 `DecisionBoundaryDisplay` 함수를 사용하여 분류기의 결정 경계를 시각화합니다.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
    clf, X, cmap=cmap_light, ax=ax, response_method="predict"
)
```
