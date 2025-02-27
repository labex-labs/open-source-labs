# Calculer des métriques

Nous pouvons calculer les coefficients, l'erreur quadratique moyenne et le coefficient de détermination.

```python
from sklearn.metrics import mean_squared_error, r2_score

# Les coefficients
print("Coefficients: \n", regr.coef_)

# L'erreur quadratique moyenne
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))

# Le coefficient de détermination : 1 est une prédiction parfaite
print("Coefficient of determination: %.2f"
      % r2_score(diabetes_y_test, diabetes_y_pred))
```
