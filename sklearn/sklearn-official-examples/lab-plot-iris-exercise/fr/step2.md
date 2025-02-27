# Préparer les données

Ensuite, nous allons préparer les données pour l'entraînement et les tests. Nous allons diviser les données en 90 % pour l'entraînement et 10 % pour les tests.

```python
n_sample = len(X)

np.random.seed(0)
order = np.random.permutation(n_sample)
X = X[order]
y = y[order].astype(float)

X_train = X[: int(0.9 * n_sample)]
y_train = y[: int(0.9 * n_sample)]
X_test = X[int(0.9 * n_sample) :]
y_test = y[int(0.9 * n_sample) :]
```
