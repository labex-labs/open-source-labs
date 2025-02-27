# Entrenar Lasso con datos densos

Ahora entrenamos dos modelos de regresión Lasso, uno con los datos densos y otro con los datos dispersos. Establecemos el parámetro alpha en 1 y el número máximo de iteraciones en 1000.

```python
alpha = 1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
```
