# Définissez les modèles à comparer

Nous allons définir deux modèles à comparer : un arbre de décision unique et un ensemble bagging d'arbres de décision.

```python
estimators = [
    ("Tree", DecisionTreeRegressor()),
    ("Bagging(Tree)", BaggingRegressor(DecisionTreeRegressor())),
]
n_estimators = len(estimators)
```
