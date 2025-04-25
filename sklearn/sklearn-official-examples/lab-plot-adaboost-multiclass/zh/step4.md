# 创建并训练模型

我们将创建两个 AdaBoost 模型，一个使用 SAMME，另一个使用 SAMME.R。两个模型都将使用最大深度为 2 且有 300 个估计器的决策树分类器。

```python
bdt_real = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2), n_estimators=300, learning_rate=1
)

bdt_discrete = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2),
    n_estimators=300,
    learning_rate=1.5,
    algorithm="SAMME",
)

bdt_real.fit(X_train, y_train)
bdt_discrete.fit(X_train, y_train)
```
