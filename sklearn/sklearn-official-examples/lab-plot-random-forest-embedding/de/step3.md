# Verwenden von RandomTreesEmbedding zum Transformieren von Daten

In diesem Schritt werden wir RandomTreesEmbedding verwenden, um die Daten zu transformieren.

```python
hasher = RandomTreesEmbedding(n_estimators=10, random_state=0, max_depth=3)
X_transformed = hasher.fit_transform(X)
```
