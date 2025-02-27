# Erstellen eines MultiOutputRegressors

Wir werden einen `MultiOutputRegressor` erstellen, der einen Random Forest Regressor als zugrunde liegenden Schätzer verwendet. Wir werden die gleichen Parameter wie in Schritt 4 verwenden.

```python
regr_multirf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=0))
regr_multirf.fit(X_train, y_train)
```
