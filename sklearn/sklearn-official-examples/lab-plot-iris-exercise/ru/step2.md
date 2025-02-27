# Подготовка данных

Далее мы подготовим данные для обучения и тестирования. Мы разделим данные на 90% для обучения и 10% для тестирования.

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
