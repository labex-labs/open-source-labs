# Ridge-Regressionswege berechnen

In diesem Schritt berechnen wir die Ridge-Regressionswege für verschiedene Regularisierungskräfte.

```python
n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)

coefs = []
for a in alphas:
    ridge = linear_model.Ridge(alpha=a, fit_intercept=False)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)
```
