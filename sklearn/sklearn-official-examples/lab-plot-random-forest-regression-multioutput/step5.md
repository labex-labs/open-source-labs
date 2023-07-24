# Create MultiOutputRegressor

We will create a `MultiOutputRegressor` using a random forest regressor as the underlying estimator. We will use the same parameters as in Step 4.

```python
regr_multirf = MultiOutputRegressor(RandomForestRegressor(n_estimators=100, max_depth=max_depth, random_state=0))
regr_multirf.fit(X_train, y_train)
```
