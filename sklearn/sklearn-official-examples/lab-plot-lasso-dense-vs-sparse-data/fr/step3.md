# Entraîner Lasso sur des données denses

Maintenant, nous entraînons deux modèles de régression Lasso, l'un sur les données denses et l'autre sur les données creuses. Nous définissons le paramètre alpha sur 1 et le nombre maximum d'itérations sur 1000.

```python
alpha = 1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
```
