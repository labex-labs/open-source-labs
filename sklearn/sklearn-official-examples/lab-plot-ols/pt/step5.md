# Calcular Métricas

Podemos calcular os coeficientes, o erro quadrático médio e o coeficiente de determinação.

```python
from sklearn.metrics import mean_squared_error, r2_score

# Os coeficientes
print("Coeficientes: \n", regr.coef_)

# O erro quadrático médio
print("Erro quadrático médio: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))

# O coeficiente de determinação: 1 é uma previsão perfeita
print("Coeficiente de determinação: %.2f"
      % r2_score(diabetes_y_test, diabetes_y_pred))
```
