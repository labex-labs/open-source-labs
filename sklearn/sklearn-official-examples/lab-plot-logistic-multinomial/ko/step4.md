# 다항 로지스틱 회귀 모델의 결정 경계 시각화

이제 scikit-learn 의 `DecisionBoundaryDisplay` 함수를 사용하여 다항 로지스틱 회귀 모델의 결정 경계를 시각화합니다. response 메서드를 `"predict"`로, 컬러맵을 `"plt.cm.Paired"`로 설정하고, 학습 데이터 포인트도 함께 플롯합니다.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
        clf, X, response_method="predict", cmap=plt.cm.Paired, ax=ax
    )
plt.title("LogisticRegression (multinomial) 의 결정 경계")
plt.axis("tight")

colors = "bry"
for i, color in zip(clf.classes_, colors):
        idx = np.where(y == i)
        plt.scatter(
            X[idx, 0], X[idx, 1], c=color, cmap=plt.cm.Paired, edgecolor="black", s=20
        )
```
