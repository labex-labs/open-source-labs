# Regressionmodell anpassen

Jetzt werden wir die Gradienten-Boosting-Regressoren initialisieren und sie an unseren Trainingsdaten anpassen. Schauen wir uns auch den mittleren quadratischen Fehler auf den Testdaten an.

```python
reg = ensemble.GradientBoostingRegressor(**params)
reg.fit(X_train, y_train)

mse = mean_squared_error(y_test, reg.predict(X_test))
print("The mean squared error (MSE) on test set: {:.4f}".format(mse))
```
