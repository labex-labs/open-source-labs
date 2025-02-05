# 标注最不确定的点

我们将把人工标注的标签添加到有标签的数据点中，并用它们来训练模型。

```python
y_train[uncertainty_index] = y[uncertainty_index]
lp_model.fit(X, y_train)
```
