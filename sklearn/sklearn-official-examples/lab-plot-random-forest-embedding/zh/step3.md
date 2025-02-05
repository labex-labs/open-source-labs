# 使用随机树嵌入变换数据

在这一步中，我们将使用随机树嵌入来变换数据。

```python
hasher = RandomTreesEmbedding(n_estimators=10, random_state=0, max_depth=3)
X_transformed = hasher.fit_transform(X)
```
