# 両方の分類器の決定関数をプロットする

`sklearn.inspection` ライブラリの `DecisionBoundaryDisplay` 関数を使って、両方の分類器の決定関数をプロットします。`plot_method` を `"contour"` に、通常の SVM の `colors` を `"k"` に、重み付き SVM の `colors` を `"r"` に、`levels` を `[0]` に、`alpha` を `0.5` に、`linestyles` を `["-"]` に設定します。また、`ax` を `plt.gca()` に設定します。

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
