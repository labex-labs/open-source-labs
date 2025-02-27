# Ausführen von GridSearchCV

Wir führen GridSearchCV durch, um die beste Kombination aus PCA-Abschneidung und Klassifizierer-Regularisierung zu finden.

```python
search = GridSearchCV(pipe, param_grid, n_jobs=2)
search.fit(X_digits, y_digits)
```
