# RandomTreesEmbeddingを使ってデータを変換する

このステップでは、RandomTreesEmbeddingを使ってデータを変換します。

```python
hasher = RandomTreesEmbedding(n_estimators=10, random_state=0, max_depth=3)
X_transformed = hasher.fit_transform(X)
```
