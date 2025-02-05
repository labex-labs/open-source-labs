# 拟合随机森林

我们将拟合一个随机森林分类器来计算特征重要性。

```python
feature_names = [f"feature {i}" for i in range(X.shape[1])]
forest = RandomForestClassifier(random_state=0)
forest.fit(X_train, y_train)
```
