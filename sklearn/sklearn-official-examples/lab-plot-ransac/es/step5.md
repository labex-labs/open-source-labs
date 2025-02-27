# Comparar coeficientes estimados

Compararemos los coeficientes estimados del modelo real, del modelo lineal y del regresor RANSAC.

```python
# Compare estimated coefficients
print("Estimated coefficients (true, linear regression, RANSAC):")
print(coef, lr.coef_, ransac.estimator_.coef_)
```
