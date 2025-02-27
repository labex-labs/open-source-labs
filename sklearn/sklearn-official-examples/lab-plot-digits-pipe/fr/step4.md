# Exécuter GridSearchCV

Nous allons exécuter GridSearchCV pour trouver la meilleure combinaison de la troncature de la PCA et de la régularisation du classifieur.

```python
search = GridSearchCV(pipe, param_grid, n_jobs=2)
search.fit(X_digits, y_digits)
```
