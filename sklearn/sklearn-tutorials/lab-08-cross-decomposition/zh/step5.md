# 典型相关分析（CCA）

#### 拟合 CCA 模型

“典型相关分析（CCA）”算法是偏最小二乘法（PLS）的一种特殊情况，代表典型相关分析。它用于找出两组变量之间的相关性。

```python
cca = CCA(n_components=2)
cca.fit(X, Y)
```

#### 转换数据

我们可以使用拟合好的模型对原始数据进行转换。转换后的数据维度将会降低。

```python
X_transformed = cca.transform(X)
Y_transformed = cca.transform(Y)
```
