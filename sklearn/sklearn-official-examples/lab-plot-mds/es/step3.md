# Añadir ruido a los datos

Luego, añadiremos ruido a las distancias entre pares de puntos de datos utilizando numpy.

```python
similarities = euclidean_distances(X_true)

# Add noise to the similarities
noise = np.random.rand(n_samples, n_samples)
noise = noise + noise.T
noise[np.arange(noise.shape[0]), np.arange(noise.shape[0])] = 0
similarities += noise
```
