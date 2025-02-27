# Ajuster un modèle avec des contraintes monotones

Nous allons maintenant ajuster un autre modèle sur les mêmes données, mais avec des contraintes monotones sur les caractéristiques. Nous allons imposer une contrainte d'augmentation monotone sur la première caractéristique et une contrainte de diminution monotone sur la seconde caractéristique.

```python
gbdt_with_monotonic_cst = HistGradientBoostingRegressor(monotonic_cst=[1, -1])
gbdt_with_monotonic_cst.fit(X, y)
```
