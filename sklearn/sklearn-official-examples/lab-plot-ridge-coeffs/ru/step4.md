# Обучаем модель с разными степенями регуляризации

Мы обучим модель с разными степенями регуляризации с использованием цикла. Мы установим степень регуляризации, изменив значение alpha в функции `set_params`. Мы сохраним коэффициенты и ошибки для каждого значения alpha.

```python
coefs = []
errors = []

alphas = np.logspace(-6, 6, 200)

for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(X, y)
    coefs.append(clf.coef_)
    errors.append(mean_squared_error(clf.coef_, w))
```
