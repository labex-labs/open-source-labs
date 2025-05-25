# 산점도에 결정 경계 표시

scikit-learn 라이브러리의 `DecisionBoundaryDisplay`를 사용하여 산점도에 결정 경계를 표시합니다.

```python
_, ax = plt.subplots(figsize=(4, 3))
DecisionBoundaryDisplay.from_estimator(
    logreg,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
    xlabel="꽃받침 길이",
    ylabel="꽃받침 너비",
    eps=0.5,
)

# 학습 데이터 포인트도 함께 표시
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors="k", cmap=plt.cm.Paired)

plt.xticks(())
plt.yticks(())

plt.show()
```
