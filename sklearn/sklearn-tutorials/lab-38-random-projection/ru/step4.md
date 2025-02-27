#稀疏随机投影

接下来，让我们尝试另一种称为稀疏随机投影的随机投影类型。

```python
transformer = random_projection.SparseRandomProjection()
X_new = transformer.fit_transform(X)
```

在这里，我们创建了`SparseRandomProjection`类的一个实例，并使用`fit_transform`方法将其应用于我们的数据`X`。结果存储在`X_new`变量中。
