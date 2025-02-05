# 定义要比较的模型

我们将定义两个模型进行比较：一个单决策树模型和一个决策树装袋集成模型。

```python
estimators = [
    ("Tree", DecisionTreeRegressor()),
    ("Bagging(Tree)", BaggingRegressor(DecisionTreeRegressor())),
]
n_estimators = len(estimators)
```
