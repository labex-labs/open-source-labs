# Entraînement du transformateur d'imbrication

`RandomTreesEmbedding` est une méthode non supervisée et ne nécessite pas d'être entraînée indépendamment.

```python
from sklearn.ensemble import RandomTreesEmbedding

random_tree_embedding = RandomTreesEmbedding(
    n_estimators=n_estimators, max_depth=max_depth, random_state=0
)

rt_model = make_pipeline(random_tree_embedding, LogisticRegression(max_iter=1000))
rt_model.fit(X_train_linear, y_train_linear)
```
