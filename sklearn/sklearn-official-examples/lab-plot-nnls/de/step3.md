# Nichtnegative kleinste Quadrate Regression anpassen

Wir werden nun unsere Daten mit der nichtnegativen kleinsten Quadrate Regression anpassen. Dies wird mit der `LinearRegression`-Klasse von scikit-learn mit dem Parameter `positive=True` durchgeführt. Anschließend werden wir die Werte für unser Testset vorhersagen und den R2-Wert berechnen.

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

reg_nnls = LinearRegression(positive=True)
y_pred_nnls = reg_nnls.fit(X_train, y_train).predict(X_test)
r2_score_nnls = r2_score(y_test, y_pred_nnls)
print("NNLS R2 score", r2_score_nnls)
```
