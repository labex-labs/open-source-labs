# 두 분류기의 결정 함수 플롯

`sklearn.inspection` 라이브러리의 `DecisionBoundaryDisplay` 함수를 사용하여 두 분류기의 결정 함수를 플롯합니다. 일반 SVM 에는 `plot_method`를 `"contour"`, `colors`를 `"k"`, 가중치 SVM 에는 `colors`를 `"r"`로 설정합니다. `levels`는 `[0]`, `alpha`는 `0.5`, `linestyles`는 `["-"]`로 설정합니다. 또한 `ax`를 `plt.gca()`로 설정합니다.

```python
ax = plt.gca()
disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[0],
    alpha=0.5,
    linestyles=["-"],
    ax=ax,
)

wdisp = DecisionBoundaryDisplay.from_estimator(
    wclf,
    X,
    plot_method="contour",
    colors="r",
    levels=[0],
    alpha=0.5,
    linestyles=["-"],
    ax=ax,
)
```
