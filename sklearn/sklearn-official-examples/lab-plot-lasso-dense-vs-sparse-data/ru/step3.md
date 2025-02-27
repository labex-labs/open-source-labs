# Обучаем Lasso на плотных данных

Теперь мы обучаем две модели Lasso-регрессии, одну на плотных данных, а другую на разреженных данных. Мы устанавливаем параметр alpha равным 1 и максимальное количество итераций равным 1000.

```python
alpha = 1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
```
