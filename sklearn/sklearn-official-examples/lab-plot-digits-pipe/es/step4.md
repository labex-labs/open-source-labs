# Realizar GridSearchCV

Realizaremos GridSearchCV para encontrar la mejor combinación de truncamiento del PCA y regularización del clasificador.

```python
search = GridSearchCV(pipe, param_grid, n_jobs=2)
search.fit(X_digits, y_digits)
```
