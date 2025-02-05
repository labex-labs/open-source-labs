# 多输出回归

## 问题描述

多输出回归为每个样本预测多个数值属性。每个属性都是一个数值变量，且属性的数量可以大于或等于两个。

## 目标格式

多输出回归目标的有效表示形式是一个密集矩阵，其中每行代表一个样本，每列代表一个不同的属性。

## 示例

让我们使用 make_regression 函数创建一个多输出回归问题：

```python
from sklearn.datasets import make_regression
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression

# 生成一个多输出回归问题
X, y = make_regression(n_samples=100, n_features=10, n_targets=3, random_state=0)

# 拟合一个多输出线性回归模型
model = MultiOutputRegressor(LinearRegression())
model.fit(X, y)

# 进行预测
predictions = model.predict(X)
print(predictions)
```
