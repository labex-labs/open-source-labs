# Daten generieren

In diesem Schritt generieren wir Daten mit der Funktion `numpy.random.RandomState` und den in Schritt 3 definierten Parametern.

```python
rng = np.random.RandomState(random_state)
X = np.vstack(
    [
        rng.multivariate_normal(means[j], covars[j], samples[j])
        for j in range(n_components)
    ]
)
y = np.concatenate([np.full(samples[j], j, dtype=int) for j in range(n_components)])
```
