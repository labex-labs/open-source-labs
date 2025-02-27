# Сравним оцененные коэффициенты

Мы сравним оцененные коэффициенты истинной модели, линейной модели и регрессора RANSAC.

```python
# Compare estimated coefficients
print("Estimated coefficients (true, linear regression, RANSAC):")
print(coef, lr.coef_, ransac.estimator_.coef_)
```
