# Entraînez un régresseur à l'aide de la SGD

Ensuite, nous allons entraîner un régresseur à l'aide de la classe SGDRegressor. Nous utiliserons la fonction de perte squared_error et la pénalité l2.

```python
# Entraînez un régresseur à l'aide de la SGD
reg = SGDRegressor(loss="squared_error", penalty="l2", max_iter=100, random_state=42)
reg.fit(X_train, y_train)

# Faites des prédictions sur l'ensemble de test
y_pred = reg.predict(X_test)

# Évaluez l'erreur quadratique moyenne du régresseur
mse = mean_squared_error(y_test, y_pred)

# Affichez l'erreur quadratique moyenne
print("Erreur quadratique moyenne du régresseur :", mse)
```
