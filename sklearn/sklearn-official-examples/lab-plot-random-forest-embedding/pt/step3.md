# Utilizar RandomTreesEmbedding para Transformar Dados

Neste passo, utilizaremos RandomTreesEmbedding para transformar os dados.

```python
hasher = RandomTreesEmbedding(n_estimators=10, random_state=0, max_depth=3)
X_transformed = hasher.fit_transform(X)
```
