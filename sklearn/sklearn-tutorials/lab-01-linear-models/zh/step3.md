# Lasso

Lasso 是一种线性回归方法，它在普通最小二乘目标函数中添加了一个惩罚项。该惩罚项具有将某些系数精确设置为零的效果，从而实现特征选择。Lasso 可用于稀疏模型估计。

让我们拟合一个 Lasso 模型。

```python
reg = linear_model.Lasso(alpha=0.1)
reg.fit([[0, 0], [1, 1]], [0, 1])

print(reg.coef_)
```

- 我们创建一个 `Lasso` 实例，将正则化参数 `alpha` 设置为 0.1。
- 我们使用 `fit` 方法将模型拟合到训练数据上。
- 我们打印 Lasso 模型的系数。
