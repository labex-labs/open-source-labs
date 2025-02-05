# 在离散化数据集上训练线性回归模型

在这一步中，我们将在离散化后的数据集上训练一个线性回归模型。

```python
reg = LinearRegression().fit(X_binned, y)
```
