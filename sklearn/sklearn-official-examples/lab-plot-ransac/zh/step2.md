# 拟合线性模型

我们将使用 scikit-learn 的 LinearRegression 类对数据拟合一个线性模型。

```python
# 使用所有数据拟合直线
lr = linear_model.LinearRegression()
lr.fit(X, y)
```
