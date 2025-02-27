# Preparar los datos

A continuación, prepararemos los datos para el entrenamiento y la prueba. Dividiremos los datos en un 90% para el entrenamiento y un 10% para la prueba.

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
