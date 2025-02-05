# 创建并拟合一个 AdaBoost 决策树

在这一步中，我们将使用 `sklearn.ensemble` 模块中的 `AdaBoostClassifier` 类创建一个 AdaBoost 决策树。我们将使用决策树作为基估计器，并将 `max_depth` 参数设置为 1。我们还将把 `algorithm` 参数设置为 "SAMME"，把 `n_estimators` 参数设置为 200。最后，我们将把分类器拟合到数据集上。

```python
bdt = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200
)

bdt.fit(X, y)
```
