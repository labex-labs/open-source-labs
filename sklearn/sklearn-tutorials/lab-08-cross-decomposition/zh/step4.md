# 典型相关分析偏最小二乘法（PLSCanonical）

#### 拟合 PLSCanonical 模型

接下来，我们将使用“典型相关分析偏最小二乘法（PLSCanonical）”算法，该算法用于找出两个矩阵之间的典型相关性。当特征之间存在多重共线性时，此算法很有用。

```python
plsc = PLSCanonical(n_components=2)
plsc.fit(X, Y)
```

#### 转换数据

我们可以使用拟合好的模型对原始数据进行转换。转换后的数据维度将会降低。

```python
X_transformed = plsc.transform(X)
Y_transformed = plsc.transform(Y)
```
