# Построение функций принятия решений для обоих классификаторов

Мы построим графики функций принятия решений для обоих классификаторов с использованием функции `DecisionBoundaryDisplay` из библиотеки `sklearn.inspection`. Мы установим `plot_method` равным `"contour"`, `colors` равным `"k"` для простого SVM и `"r"` для взвешенного SVM, `levels` равным `[0]`, `alpha` равным `0.5` и `linestyles` равным `["-"]`. Также установим `ax` равным `plt.gca()`.

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
