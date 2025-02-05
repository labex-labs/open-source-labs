# 高斯随机投影

现在，让我们应用高斯随机投影来降低数据的维度。

```python
transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
```

在这一步中，我们创建了一个 `GaussianRandomProjection` 类的实例，并将其应用于我们的数据 `X`。然后，我们通过调用 `fit_transform` 方法来应用变换。结果存储在 `X_new` 变量中。
