# 转换后的数据集

我们将使用组合特征来转换数据集。

```python
X_features = combined_features.fit(X, y).transform(X)
print("Combined space has", X_features.shape[1], "features")
```
