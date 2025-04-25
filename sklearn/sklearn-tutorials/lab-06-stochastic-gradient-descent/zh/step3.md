# 数据预处理

在应用随机梯度下降（SGD）之前，对数据进行预处理通常是有益的。在这种情况下，我们将使用 scikit-learn 的 StandardScaler 对特征进行标准化。

```python
scaler = StandardScaler()
X = scaler.fit_transform(X)
```
