# Entrenar Lasso con datos dispersos

Ahora entrenamos dos modelos de regresión Lasso, uno con los datos densos y otro con los datos dispersos. Establecemos el parámetro alpha en 0.1 y el número máximo de iteraciones en 10000.

```python
alpha = 0.1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
```
