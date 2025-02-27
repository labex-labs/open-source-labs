# Schätzer anpassen

Der zweite Schritt besteht darin, die multi-output-Schätzer an die Trainingsdaten anzupassen. Wir werden vier verschiedene Algorithmen verwenden: extrem zufällige Bäume, k-nearest neighbors, lineare Regression und Ridge Regression. Die Schätzer werden die untere Hälfte der Gesichter anhand der oberen Hälfte vorherzusagen.

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
