# 创建逻辑回归分类器实例并拟合数据

我们将创建一个逻辑回归分类器实例并拟合数据。

```python
# 创建逻辑回归分类器实例并拟合数据。
logreg = LogisticRegression(C=1e5)
logreg.fit(X, Y)
```
