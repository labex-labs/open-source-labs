# 绘制两个分类器的决策函数

我们将使用 `sklearn.inspection` 库中的 `DecisionBoundaryDisplay` 函数来绘制两个分类器的决策函数。我们将把 `plot_method` 设置为 `"contour"`，普通支持向量机（SVM）的 `colors` 设置为 `"k"`，加权支持向量机的 `colors` 设置为 `"r"`，`levels` 设置为 `[0]`，`alpha` 设置为 `0.5`，`linestyles` 设置为 `["-"]`。我们还将把 `ax` 设置为 `plt.gca()`。

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
