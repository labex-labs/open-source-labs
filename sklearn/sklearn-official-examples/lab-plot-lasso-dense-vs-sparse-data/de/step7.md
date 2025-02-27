# Lasso auf spärlichen Daten trainieren

Jetzt trainieren wir zwei Lasso-Regressionsmodelle, eines auf den dichten Daten und eines auf den spärlichen Daten. Wir setzen den `alpha`-Parameter auf 0,1 und die maximale Anzahl an Iterationen auf 10000.

```python
alpha = 0.1
sparse_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
dense_lasso = Lasso(alpha=alpha, fit_intercept=False, max_iter=10000)
```
