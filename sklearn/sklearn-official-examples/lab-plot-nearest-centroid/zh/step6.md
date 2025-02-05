# 可视化决策边界

我们使用 Scikit-learn 中的 DecisionBoundaryDisplay 函数来可视化分类器的决策边界。

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
    clf, X, cmap=cmap_light, ax=ax, response_method="predict"
)
```
