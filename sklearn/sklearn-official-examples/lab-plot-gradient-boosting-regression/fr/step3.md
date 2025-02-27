# Ajuster le modèle de régression

Maintenant, nous allons initialiser les régresseurs Gradient Boosting et l'ajuster avec nos données d'entraînement. Regardons également l'erreur quadratique moyenne sur les données de test.

```python
reg = ensemble.GradientBoostingRegressor(**params)
reg.fit(X_train, y_train)

mse = mean_squared_error(y_test, reg.predict(X_test))
print("The mean squared error (MSE) on test set: {:.4f}".format(mse))
```
