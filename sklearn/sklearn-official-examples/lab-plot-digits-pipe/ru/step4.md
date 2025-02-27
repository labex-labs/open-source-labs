# Выполняем GridSearchCV

Мы выполним GridSearchCV, чтобы найти наилучшую комбинацию усечения PCA и регуляризации классификатора.

```python
search = GridSearchCV(pipe, param_grid, n_jobs=2)
search.fit(X_digits, y_digits)
```
