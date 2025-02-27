# Création d'un ensemble de données

Nous créons un ensemble de données avec deux ensembles de données bidimensionnels multivariés co-variant, X et Y. Nous extrayons ensuite les directions de covariance, c'est-à-dire les composantes de chaque ensemble de données qui expliquent la variance partagée la plus importante entre les deux ensembles de données.

```python
import numpy as np

n = 500
# 2 variables latentes :
l1 = np.random.normal(size=n)
l2 = np.random.normal(size=n)

latentes = np.array([l1, l1, l2, l2]).T
X = latentes + np.random.normal(size=4 * n).reshape((n, 4))
Y = latentes + np.random.normal(size=4 * n).reshape((n, 4))

X_train = X[: n // 2]
Y_train = Y[: n // 2]
X_test = X[n // 2 :]
Y_test = Y[n // 2 :]

print("Corr(X)")
print(np.round(np.corrcoef(X.T), 2))
print("Corr(Y)")
print(np.round(np.corrcoef(Y.T), 2))
```
