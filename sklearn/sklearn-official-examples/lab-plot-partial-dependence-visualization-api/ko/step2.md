# 두 특징에 대한 부분 의존성 플롯

이 단계에서는 의사 결정 트리에 대해 "나이"와 "BMI"(체질량 지수) 라는 두 특징에 대한 부분 의존성 곡선을 플롯합니다. 두 개의 특징을 사용하면 `PartialDependenceDisplay.from_estimator`는 두 개의 곡선을 플롯할 것으로 예상합니다. 여기서 플롯 함수는 `ax`에 의해 정의된 공간을 사용하여 두 개의 플롯 그리드를 배치합니다.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("의사 결정 트리")
tree_disp = PartialDependenceDisplay.from_estimator(tree, X, ["age", "bmi"], ax=ax)
```

다층 퍼셉트론에 대해서도 부분 의존성 곡선을 플롯할 수 있습니다. 이 경우 `line_kw`를 `PartialDependenceDisplay.from_estimator`에 전달하여 곡선의 색상을 변경합니다.

```python
fig, ax = plt.subplots(figsize=(12, 6))
ax.set_title("다층 퍼셉트론")
mlp_disp = PartialDependenceDisplay.from_estimator(
    mlp, X, ["age", "bmi"], ax=ax, line_kw={"color": "red"}
)
```
