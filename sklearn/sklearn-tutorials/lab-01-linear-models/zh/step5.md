# 随机梯度下降（SGD）

随机梯度下降（SGD）是一种用于训练线性模型的简单而高效的方法。当样本数量和特征数量非常大时，它特别有用。SGD 在每次迭代时使用一小部分训练数据来更新模型参数，这使得它适用于在线学习和核外学习。

让我们使用 SGD 拟合一个逻辑回归模型。

```python
clf = linear_model.SGDClassifier(loss="log_loss", max_iter=1000)
clf.fit(X, y)

print(clf.coef_)
```

- 我们创建一个 `SGDClassifier` 实例，将 `loss` 参数设置为 "log_loss" 以执行逻辑回归。
- 我们使用 `fit` 方法将模型拟合到训练数据上。
- 我们打印使用 SGD 获得的逻辑回归模型的系数。
