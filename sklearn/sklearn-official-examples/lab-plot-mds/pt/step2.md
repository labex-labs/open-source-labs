# Gerar Dados

Em seguida, geraremos um conjunto de dados ruidoso usando numpy. Geraremos 20 amostras com 2 recursos cada.

```python
EPSILON = np.finfo(np.float32).eps
n_samples = 20
seed = np.random.RandomState(seed=3)
X_true = seed.randint(0, 20, 2 * n_samples).astype(float)
X_true = X_true.reshape((n_samples, 2))
# Centralizar os dados
X_true -= X_true.mean()
```
