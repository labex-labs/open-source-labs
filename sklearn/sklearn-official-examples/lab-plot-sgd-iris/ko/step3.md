# 결정 경계 시각화

이제 학습된 모델의 결정 경계를 iris 데이터셋에서 시각화합니다. DecisionBoundaryDisplay 클래스를 사용하여 모델의 결정 경계를 시각화합니다.

```python
from sklearn.inspection import DecisionBoundaryDisplay

ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    xlabel=iris.feature_names[0],
    ylabel=iris.feature_names[1],
)
plt.axis("tight")
```
