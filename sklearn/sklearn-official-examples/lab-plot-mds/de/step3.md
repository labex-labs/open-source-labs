# Rauschen zu den Daten hinzufügen

Anschließend werden wir mit numpy Rauschen zu den paarweisen Distanzen zwischen den Datenpunkten hinzufügen.

```python
similarities = euclidean_distances(X_true)

# Add noise to the similarities
noise = np.random.rand(n_samples, n_samples)
noise = noise + noise.T
noise[np.arange(noise.shape[0]), np.arange(noise.shape[0])] = 0
similarities += noise
```
