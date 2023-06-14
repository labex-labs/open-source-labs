# Perform GridSearchCV

We will perform GridSearchCV to find the best combination of PCA truncation and classifier regularization.

```python
search = GridSearchCV(pipe, param_grid, n_jobs=2)
search.fit(X_digits, y_digits)
```


