# Ajuster la forêt aléatoire

Nous allons ajuster un classifieur à forêt aléatoire pour calculer les importances des caractéristiques.

```python
feature_names = [f"feature {i}" for i in range(X.shape[1])]
forest = RandomForestClassifier(random_state=0)
forest.fit(X_train, y_train)
```
