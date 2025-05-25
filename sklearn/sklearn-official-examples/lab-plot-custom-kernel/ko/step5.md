# 결정 경계 시각화

이 단계에서는 결정 경계와 지지 벡터를 시각화합니다. scikit-learn 의 검사 모듈에서 `DecisionBoundaryDisplay` 모듈을 사용하여 결정 경계를 그립니다. 또한 학습 데이터 포인트를 산점도로 표시합니다.

```python
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
)

plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolors="k")
plt.title("사용자 지정 커널을 사용한 서포트 벡터 머신을 이용한 3 클래스 분류")
plt.axis("tight")
plt.show()
```
