# 可视化决策面

现在，我们将在鸢尾花数据集上绘制训练好的模型的决策面。我们将使用 `DecisionBoundaryDisplay` 类来可视化模型的决策边界。

```python
from sklearn.inspection import DecisionBoundaryDisplay

ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    xlabel=iris.feature_names[0],
    ylabel=iris.feature_names[1],
)
plt.axis("tight")
```
