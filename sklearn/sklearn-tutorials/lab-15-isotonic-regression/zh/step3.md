# 拟合保序回归模型

现在，我们可以将保序回归模型拟合到我们的数据上。我们创建一个 `IsotonicRegression` 类的实例，并使用我们的输入数据和目标值调用 `fit` 方法。

```python
# 拟合保序回归模型
ir = IsotonicRegression()
ir.fit(X, y)
```
