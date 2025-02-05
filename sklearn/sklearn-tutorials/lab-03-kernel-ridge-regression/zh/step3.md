# 拟合核岭回归模型

现在，让我们将核岭回归模型拟合到数据上。我们将使用径向基函数（RBF）核，它常用于非线性回归。

```python
# 拟合核岭回归模型
alpha = 1.0  # 正则化参数
gamma = 0.1  # RBF 核的核系数
krr = KernelRidge(alpha=alpha, kernel='rbf', gamma=gamma)
krr.fit(X, y)
```
