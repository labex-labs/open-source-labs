# 保持特征数量不变

默认情况下，scikit-learn 插补器会删除仅包含缺失值的列。然而，在某些情况下，有必要保留空特征以保持数据的形状。我们可以通过将`keep_empty_features`参数设置为 True 来实现这一点。

```python
imputer = SimpleImputer(keep_empty_features=True)
X = np.array([[np.nan, 1], [np.nan, 2], [np.nan, 3]])
imputed_X = imputer.fit_transform(X)
```
