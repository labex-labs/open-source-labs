# Criar um conjunto de dados aleatório

Criaremos um conjunto de dados aleatório usando o NumPy e adicionaremos algum ruído a ele.

```python
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))
```
