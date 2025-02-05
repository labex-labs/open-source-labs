# 偏最小二乘回归（PLSRegression）

#### 拟合PLSRegression模型

我们将从“偏最小二乘回归（PLSRegression）”算法开始，它是一种正则化线性回归形式。我们将把这个模型拟合到我们的数据上。

```python
pls = PLSRegression(n_components=2)
pls.fit(X, Y)
```

#### 转换数据

我们可以使用拟合好的模型对原始数据进行转换。转换后的数据维度将会降低。

```python
X_transformed = pls.transform(X)
Y_transformed = pls.transform(Y)
```
