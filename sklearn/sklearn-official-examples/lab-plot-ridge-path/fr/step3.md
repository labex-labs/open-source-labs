# Calculer les chemins de régression 岭

Dans cette étape, nous allons calculer les chemins de régression 岭 pour différentes forces de régularisation.

```python
n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)

coefs = []
for a in alphas:
    ridge = linear_model.Ridge(alpha=a, fit_intercept=False)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)
```
