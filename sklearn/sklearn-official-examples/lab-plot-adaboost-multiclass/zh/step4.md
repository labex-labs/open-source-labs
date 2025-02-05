# 创建并训练模型

我们将创建两个AdaBoost模型，一个使用SAMME，另一个使用SAMME.R。两个模型都将使用最大深度为2且有300个估计器的决策树分类器。

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
