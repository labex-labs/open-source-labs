# Fit Estimators

The second step is to fit the multi-output estimators to the training data. We will use four different algorithms: extremely randomized trees, k-nearest neighbors, linear regression, and ridge regression. The estimators will predict the lower half of the faces based on the upper half.

```python
# Fit estimators
ESTIMATORS = {
    "Extra trees": ExtraTreesRegressor(
        n_estimators=10, max_features=32, random_state=0
    ),
    "K-nn": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),
}

y_test_predict = dict()
for name, estimator in ESTIMATORS.items():
    estimator.fit(X_train, y_train)
    y_test_predict[name] = estimator.predict(X_test)
```


