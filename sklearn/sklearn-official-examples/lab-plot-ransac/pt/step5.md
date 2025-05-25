# Comparar coeficientes estimados

Vamos comparar os coeficientes estimados do modelo verdadeiro, do modelo linear e do regressor RANSAC.

```python
# Comparar coeficientes estimados
print("Coeficientes estimados (verdadeiro, regressão linear, RANSAC):")
print(coef, lr.coef_, ransac.estimator_.coef_)
```
