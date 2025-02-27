# Использование RandomTreesEmbedding для преобразования данных

В этом шаге мы будем использовать RandomTreesEmbedding для преобразования данных.

```python
hasher = RandomTreesEmbedding(n_estimators=10, random_state=0, max_depth=3)
X_transformed = hasher.fit_transform(X)
```
