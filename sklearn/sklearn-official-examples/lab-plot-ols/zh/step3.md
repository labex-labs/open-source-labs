# 训练模型

现在，我们创建一个线性回归对象，并使用训练集来训练模型。

```python
from sklearn import linear_model

# 创建线性回归对象
regr = linear_model.LinearRegression()

# 使用训练集训练模型
regr.fit(diabetes_X_train, diabetes_y_train)
```
