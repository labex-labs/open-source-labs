# Добавление шума к данным

Затем мы добавим шум к попарным расстояниям между точками данных с использованием numpy.

```python
similarities = euclidean_distances(X_true)

# Add noise to the similarities
noise = np.random.rand(n_samples, n_samples)
noise = noise + noise.T
noise[np.arange(noise.shape[0]), np.arange(noise.shape[0])] = 0
similarities += noise
```
