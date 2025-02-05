# 分割数据集

我们将把数据集分割为训练集和测试集，使用前3000个样本进行训练，其余样本用于测试。

```python
n_split = 3000
X_train, X_test = X[:n_split], X[n_split:]
y_train, y_test = y[:n_split], y[n_split:]
```
