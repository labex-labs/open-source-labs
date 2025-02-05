# 重新排列打乱后的数据集

我们使用numpy中的 `argsort()` 函数重新排列打乱后的数据集，以使双聚类相邻。

```python
fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]
```
