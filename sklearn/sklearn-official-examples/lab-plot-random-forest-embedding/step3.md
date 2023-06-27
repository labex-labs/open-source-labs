# Use RandomTreesEmbedding to Transform Data

In this step, we will use RandomTreesEmbedding to transform data.

```python
hasher = RandomTreesEmbedding(n_estimators=10, random_state=0, max_depth=3)
X_transformed = hasher.fit_transform(X)
```
