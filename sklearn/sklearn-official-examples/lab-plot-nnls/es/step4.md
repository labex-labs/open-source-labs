# Ajustar la regresión lineal clásica

Ahora ajustaremos nuestros datos utilizando la regresión lineal clásica. Esto se hace utilizando la clase `LinearRegression` de scikit-learn. Luego, predecirá los valores para nuestro conjunto de prueba y calculará la puntuación R2.

```python
reg_ols = LinearRegression()
y_pred_ols = reg_ols.fit(X_train, y_train).predict(X_test)
r2_score_ols = r2_score(y_test, y_pred_ols)
print("OLS R2 score", r2_score_ols)
```
