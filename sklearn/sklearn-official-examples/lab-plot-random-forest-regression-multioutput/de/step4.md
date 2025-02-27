# Erstellen eines Random Forest Regressors

Wir werden einen Random Forest Regressor mit einer maximalen Tiefe von 30 und 100 Schätzern mit der `RandomForestRegressor` von scikit-learn erstellen.

```python
max_depth = 30
regr_rf = RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=2)
regr_rf.fit(X_train, y_train)
```
