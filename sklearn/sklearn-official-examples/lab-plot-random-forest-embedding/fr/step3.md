# Utiliser RandomTreesEmbedding pour transformer les données

Dans cette étape, nous allons utiliser RandomTreesEmbedding pour transformer les données.

```python
hasher = RandomTreesEmbedding(n_estimators=10, random_state=0, max_depth=3)
X_transformed = hasher.fit_transform(X)
```
