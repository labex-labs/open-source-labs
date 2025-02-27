# 決定境界の描画

このステップでは、決定面とサポートベクトルを描画します。scikit-learn の inspection モジュールから DecisionBoundaryDisplay モジュールを使って決定境界を描画します。また、訓練ポイントを散布図で描画します。

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
plt.title("3-Class classification using Support Vector Machine with custom kernel")
plt.axis("tight")
plt.show()
```
