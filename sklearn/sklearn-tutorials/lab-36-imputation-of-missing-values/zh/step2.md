# 使用 SimpleImputer 进行单变量特征插补

`SimpleImputer`类提供了以单变量方式插补缺失值的基本策略。我们可以从不同的策略中进行选择，例如用常数值替换缺失值，或者使用每列的均值、中位数或最频繁值来插补缺失值。

让我们先考虑均值策略。我们将创建一个`SimpleImputer`实例，并在我们的数据上进行拟合，以学习插补策略。然后，我们可以使用`transform`方法根据学到的策略插补缺失值。

```python
imp = SimpleImputer(strategy='mean')
X = [[1, 2], [np.nan, 3], [7, 6]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [7, 6]]
imputed_X_test = imp.transform(X_test)
```
