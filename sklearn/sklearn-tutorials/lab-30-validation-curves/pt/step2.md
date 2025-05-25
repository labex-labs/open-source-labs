# Embaralhar os Dados

Para garantir aleatoriedade em nossa análise, vamos embaralhar a ordem das amostras em nosso conjunto de dados.

```python
indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]
```
