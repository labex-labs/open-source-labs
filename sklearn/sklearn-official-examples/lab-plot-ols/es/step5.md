# Calcular métricas

Podemos calcular los coeficientes, el error cuadrático medio y el coeficiente de determinación.

```python
from sklearn.metrics import mean_squared_error, r2_score

# Los coeficientes
print("Coefficients: \n", regr.coef_)

# El error cuadrático medio
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))

# El coeficiente de determinación: 1 es una predicción perfecta
print("Coefficient of determination: %.2f"
      % r2_score(diabetes_y_test, diabetes_y_pred))
```
