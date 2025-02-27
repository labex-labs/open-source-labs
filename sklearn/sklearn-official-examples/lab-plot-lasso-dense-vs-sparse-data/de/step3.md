# Lasso auf dichten Daten trainieren

Jetzt trainieren wir zwei Lasso-Regressionsmodelle, eines auf den dichten Daten und eines auf den spärlichen Daten. Wir setzen den `alpha`-Parameter auf 1 und die maximale Anzahl an Iterationen auf 1000.

```python
alpha = 1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=1000)
```
