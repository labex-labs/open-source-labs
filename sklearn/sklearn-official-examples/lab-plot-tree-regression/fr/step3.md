# Ajustez le modèle de régression

Nous allons ajuster des modèles de régression avec deux profondeurs maximales différentes : 2 et 5.

```python
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, y)
regr_2.fit(X, y)
```
