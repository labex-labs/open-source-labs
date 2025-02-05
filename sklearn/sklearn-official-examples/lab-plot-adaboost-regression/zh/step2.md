# 使用决策树和 AdaBoost 回归器进行训练和预测

我们现在定义分类器并将它们拟合到数据上。我们将第一个回归器定义为一个 `max_depth=4` 的 `DecisionTreeRegressor`。我们将第二个回归器定义为一个以 `max_depth=4` 的 `DecisionTreeRegressor` 作为基学习器的 `AdaBoostRegressor`。我们使用 300 个这样的基学习器构建 AdaBoost 回归器。然后，我们将这两个回归器都拟合到数据上，并在相同的数据上进行预测，以查看它们的拟合效果如何。

```python
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor

regr_1 = DecisionTreeRegressor(max_depth=4)

regr_2 = AdaBoostRegressor(
    DecisionTreeRegressor(max_depth=4), n_estimators=300, random_state=rng
)

regr_1.fit(X, y)
regr_2.fit(X, y)

y_1 = regr_1.predict(X)
y_2 = regr_2.predict(X)
```
