# 逻辑回归

逻辑回归是一种分类方法，它使用逻辑函数来估计可能结果的概率。它通常用于二元分类任务。逻辑回归也可以扩展以处理多类分类问题。

让我们拟合一个逻辑回归模型。

```python
clf = linear_model.LogisticRegression(random_state=0).fit(X, y)
print(clf.coef_)
```

- 我们创建一个 `LogisticRegression` 实例，将 `random_state` 参数设置为 0。
- 我们使用 `fit` 方法将模型拟合到训练数据上。
- 我们打印逻辑回归模型的系数。
