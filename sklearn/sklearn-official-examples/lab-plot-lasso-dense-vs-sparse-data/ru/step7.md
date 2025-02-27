# Обучаем Lasso на разреженных данных

Теперь мы обучаем две модели Lasso-регрессии, одну на плотных данных, а другую на разреженных данных. Мы устанавливаем параметр alpha равным 0.1 и максимальное количество итераций равным 10000.

```python
alpha = 0.1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
```
