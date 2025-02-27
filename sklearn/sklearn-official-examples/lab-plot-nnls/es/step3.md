# Ajustar la regresión de mínimos cuadrados no negativos

Ahora ajustaremos nuestros datos utilizando la regresión de mínimos cuadrados no negativos. Esto se hace utilizando la clase `LinearRegression` de scikit-learn con el parámetro `positive=True`. Luego, predecirá los valores para nuestro conjunto de prueba y calculará la puntuación R2.

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

reg_nnls = LinearRegression(positive=True)
y_pred_nnls = reg_nnls.fit(X_train, y_train).predict(X_test)
r2_score_nnls = r2_score(y_test, y_pred_nnls)
print("NNLS R2 score", r2_score_nnls)
```
