# Usar RandomTreesEmbedding para transformar datos

En este paso, usaremos RandomTreesEmbedding para transformar los datos.

```python
hasher = RandomTreesEmbedding(n_estimators=10, random_state=0, max_depth=3)
X_transformed = hasher.fit_transform(X)
```
