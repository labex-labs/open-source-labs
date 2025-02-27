# Klassische lineare Regression anpassen

Wir werden nun unsere Daten mit der klassischen linearen Regression anpassen. Dies wird mit der `LinearRegression`-Klasse von scikit-learn durchgeführt. Anschließend werden wir die Werte für unser Testset vorhersagen und den R2-Wert berechnen.

```python
reg_ols = LinearRegression()
y_pred_ols = reg_ols.fit(X_train, y_train).predict(X_test)
r2_score_ols = r2_score(y_test, y_pred_ols)
print("OLS R2 score", r2_score_ols)
```
