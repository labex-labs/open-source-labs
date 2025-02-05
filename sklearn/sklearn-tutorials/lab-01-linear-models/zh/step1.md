# 普通最小二乘法

> 如果你没有机器学习的任何先验经验，请从 [监督学习：回归](https://labex.io/courses/supervised-learning-regression) 开始。

普通最小二乘法（OLS）是一种线性回归方法，它使观测目标与预测目标之间的平方差之和最小化。在数学上，它解决的是如下形式的问题：
$$\min_{w} || X w - y||_2^2$$

让我们开始使用 OLS 拟合一个线性回归模型。

```python
from sklearn import linear_model

reg = linear_model.LinearRegression()
X = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
reg.fit(X, y)

print(reg.coef_)
```

- 我们从 scikit-learn 中导入 `linear_model` 模块。
- 我们创建一个 `LinearRegression` 的实例。
- 我们使用 `fit` 方法将模型拟合到训练数据上。
- 我们打印线性模型的系数。
