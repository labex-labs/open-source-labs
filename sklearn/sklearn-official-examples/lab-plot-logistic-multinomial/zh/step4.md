# 绘制多项式逻辑回归模型的决策边界

现在我们将使用 scikit-learn 中的`DecisionBoundaryDisplay`函数绘制多项式逻辑回归模型的决策面。我们将响应方法设置为`"predict"`，颜色映射设置为`"plt.cm.Paired"`，并绘制训练点。

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
        clf, X, response_method="predict", cmap=plt.cm.Paired, ax=ax
    )
plt.title("Decision surface of LogisticRegression (multinomial)")
plt.axis("tight")

colors = "bry"
for i, color in zip(clf.classes_, colors):
        idx = np.where(y == i)
        plt.scatter(
            X[idx, 0], X[idx, 1], c=color, cmap=plt.cm.Paired, edgecolor="black", s=20
        )
```
