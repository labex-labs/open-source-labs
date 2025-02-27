# Entraîner un modèle d'arbre de décision

Dans cette étape, nous allons entraîner un modèle d'arbre de décision sur l'ensemble de données original.

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X, y)
```
