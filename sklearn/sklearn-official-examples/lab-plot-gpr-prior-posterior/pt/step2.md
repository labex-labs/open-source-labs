# Criar dados de treino

Em seguida, criamos um conjunto de dados de treino que usaremos nas diferentes seções.

```python
rng = np.random.RandomState(4)
X_train = rng.uniform(0, 5, 10).reshape(-1, 1)
y_train = np.sin((X_train[:, 0] - 2.5) ** 2)
n_samples = 5
```
