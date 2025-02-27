# Сравниваем коэффициенты плотного и разреженного Lasso

Мы сравниваем коэффициенты модели плотного Lasso и модели разреженного Lasso, чтобы убедиться, что они дают одинаковые результаты. Мы вычисляем евклидову норму разницы между коэффициентами.

```python
coeff_diff = linalg.norm(sparse_lasso.coef_ - dense_lasso.coef_)
print(f"Distance between coefficients : {coeff_diff:.2e}")
```
