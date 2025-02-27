# Ajuster la régression linéaire classique

Nous allons maintenant ajuster nos données en utilisant la régression linéaire classique. Cela se fait en utilisant la classe `LinearRegression` de scikit-learn. Nous prédirons ensuite les valeurs pour notre ensemble de test et calculerons le score R2.

```python
reg_ols = LinearRegression()
y_pred_ols = reg_ols.fit(X_train, y_train).predict(X_test)
r2_score_ols = r2_score(y_test, y_pred_ols)
print("OLS R2 score", r2_score_ols)
```
