# Create Random Forest Regressor

We will create a random forest regressor with a maximum depth of 30 and 100 estimators using scikit-learn's `RandomForestRegressor`.

```python
max_depth = 30
regr_rf = RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=2)
regr_rf.fit(X_train, y_train)
```
