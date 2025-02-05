# 拟合线性回归模型

接下来，我们对训练集拟合一个线性回归模型。

```python
from sklearn import linear_model

ols = linear_model.LinearRegression()
_ = ols.fit(X_train, y_train)
```
