# 拟合Bagging分类器

现在，我们将在训练数据上拟合一个Bagging分类器。Bagging分类器是一种集成方法，它使用自助采样来创建多个基模型（通常是决策树），并通过多数投票来聚合它们的预测结果。

```python
bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10)
bagging.fit(X_train, y_train)
```
