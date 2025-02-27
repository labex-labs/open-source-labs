# Ajouter du bruit aux données

Nous allons ensuite ajouter du bruit aux distances entre paires de points de données à l'aide de numpy.

```python
similarities = euclidean_distances(X_true)

# Add noise to the similarities
noise = np.random.rand(n_samples, n_samples)
noise = noise + noise.T
noise[np.arange(noise.shape[0]), np.arange(noise.shape[0])] = 0
similarities += noise
```
