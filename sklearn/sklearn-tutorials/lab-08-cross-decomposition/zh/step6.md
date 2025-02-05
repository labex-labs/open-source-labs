# 偏最小二乘奇异值分解（PLSSVD）

#### 拟合PLSSVD模型

“偏最小二乘奇异值分解（PLSSVD）”算法是“典型相关分析偏最小二乘法（PLSCanonical）”的简化版本，它仅对交叉协方差矩阵计算一次奇异值分解（SVD）。当成分数量限制为1时，此算法很有用。

```python
plssvd = PLSSVD(n_components=1)
plssvd.fit(X, Y)
```

#### 转换数据

我们可以使用拟合好的模型对原始数据进行转换。转换后的数据维度将会降低。

```python
X_transformed = plssvd.transform(X)
Y_transformed = plssvd.transform(Y)
```
