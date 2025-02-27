# Daten generieren

Als nächstes werden wir mit numpy einen rauschenden Datensatz generieren. Wir werden 20 Stichproben mit jeweils 2 Merkmalen generieren.

```python
EPSILON = np.finfo(np.float32).eps
n_samples = 20
seed = np.random.RandomState(seed=3)
X_true = seed.randint(0, 20, 2 * n_samples).astype(float)
X_true = X_true.reshape((n_samples, 2))
# Center the data
X_true -= X_true.mean()
```
