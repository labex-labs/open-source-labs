# 绘制决策边界

在这一步中，我们将绘制决策面和支持向量。我们将使用 scikit-learn 的 inspection 模块中的 DecisionBoundaryDisplay 模块来绘制决策边界。我们还将绘制训练点的散点图。

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
