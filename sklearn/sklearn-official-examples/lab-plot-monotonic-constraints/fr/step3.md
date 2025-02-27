# Ajuster un modèle sans contraintes

Nous allons ajuster un modèle sur les données générées sans aucune contrainte pour voir comment le modèle se comporte sans restrictions.

```python
gbdt_no_cst = HistGradientBoostingRegressor()
gbdt_no_cst.fit(X, y)
```
