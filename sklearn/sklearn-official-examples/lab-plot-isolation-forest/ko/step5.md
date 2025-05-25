# 경로 길이 결정 경계 시각화

`response_method="decision_function"`을 설정하면 `DecisionBoundaryDisplay`의 배경은 관측치의 정상성 척도를 나타냅니다. 이러한 점수는 무작위 트리의 숲에서 평균화된 경로 길이에 의해 주어지며, 이는 특정 샘플을 분리하는 데 필요한 리프의 깊이 (또는 동등하게 분할 횟수) 에 의해 결정됩니다.

```python
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    response_method="decision_function",
    alpha=0.5,
)
disp.ax_.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
disp.ax_.set_title("IsolationForest 의 경로 길이 결정 경계")
plt.axis("square")
plt.legend(handles=handles, labels=["이상치", "내부 데이터 포인트"], title="실제 클래스")
plt.colorbar(disp.ax_.collections[1])
plt.show()
```
