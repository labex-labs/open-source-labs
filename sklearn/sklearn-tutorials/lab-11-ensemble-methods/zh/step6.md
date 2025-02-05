# 拟合随机森林分类器

接下来，我们将在训练数据上拟合一个随机森林分类器。随机森林分类器也是一种集成方法，它使用自助采样来创建多个决策树，但它还通过在每次划分时仅考虑特征的一个子集来增加额外的随机性。

```python
random_forest = RandomForestClassifier(n_estimators=10)
random_forest.fit(X_train, y_train)
```
