# Executar GridSearchCV

Executaremos GridSearchCV para encontrar a melhor combinação de truncamento do PCA e regularização do classificador.

```python
search = GridSearchCV(pipe, param_grid, n_jobs=2)
search.fit(X_digits, y_digits)
```
