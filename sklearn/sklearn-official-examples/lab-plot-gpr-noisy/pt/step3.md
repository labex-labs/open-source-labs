# Adicionando Ruído

Nesta etapa, adicionaremos algum ruído aos dados gerados para criar um conjunto de dados de treinamento mais realista.

```python
rng = np.random.RandomState(0)
X_train = rng.uniform(0, 5, size=20).reshape(-1, 1)
y_train = target_generator(X_train, add_noise=True)
```
