# Настройка регрессоров

Мы пытаемся использовать полином степени 10, чтобы потенциально получить переобучение, хотя байесовские линейные модели нормализуют размер коэффициентов полинома. Поскольку `fit_intercept=True` по умолчанию для ARDRegression и BayesianRidge, то PolynomialFeatures не должен вводить дополнительную биас-признак. Задав `return_std=True`, байесовские регрессоры возвращают стандартное отклонение постериорного распределения для параметров модели.

```python
ard_poly = make_pipeline(
    PolynomialFeatures(degree=10, include_bias=False),
    StandardScaler(),
    ARDRegression(),
).fit(X, y)
brr_poly = make_pipeline(
    PolynomialFeatures(degree=10, include_bias=False),
    StandardScaler(),
    BayesianRidge(),
).fit(X, y)

y_ard, y_ard_std = ard_poly.predict(X_plot, return_std=True)
y_brr, y_brr_std = brr_poly.predict(X_plot, return_std=True)
```
