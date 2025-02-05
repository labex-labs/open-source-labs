# 逆变换

随机投影变换器有一种计算投影矩阵逆矩阵的选项。让我们通过对投影后的数据应用逆变换来探索此功能。

```python
transformer = random_projection.SparseRandomProjection(compute_inverse_components=True)
X_new = transformer.fit_transform(X)

# 计算逆变换
X_new_inversed = transformer.inverse_transform(X_new)
```

在这一步中，我们创建了一个 `SparseRandomProjection` 类的实例，并将 `compute_inverse_components` 参数设置为 `True`。然后，我们将变换器应用于数据 `X` 并进行变换。最后，我们通过对投影后的数据 `X_new` 调用 `inverse_transform` 方法来计算逆变换。
