# Вычисляем пути Регуляризованной линейной регрессии (Ridge Regression)

В этом шаге мы вычислим пути Регуляризованной линейной регрессии для различных значений коэффициента регуляризации.

```python
n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)

coefs = []
for a in alphas:
    ridge = linear_model.Ridge(alpha=a, fit_intercept=False)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)
```
