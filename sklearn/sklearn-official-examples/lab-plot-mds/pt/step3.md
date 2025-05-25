# Adicionar Ruído aos Dados

Em seguida, adicionaremos ruído às distâncias de pares entre os pontos de dados usando numpy.

```python
similarities = euclidean_distances(X_true)

# Adicionar ruído às similaridades
noise = np.random.rand(n_samples, n_samples)
noise = noise + noise.T
noise[np.arange(noise.shape[0]), np.arange(noise.shape[0])] = 0
similarities += noise
```
