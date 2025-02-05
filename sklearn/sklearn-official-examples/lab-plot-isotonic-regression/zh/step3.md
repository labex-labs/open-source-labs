# 拟合保序回归和线性回归模型

现在我们将对生成的数据拟合保序回归模型和线性回归模型。

```python
ir = IsotonicRegression(out_of_bounds="clip")
y_ = ir.fit_transform(x, y)

lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)  # x需要为二维数据以用于线性回归
```
