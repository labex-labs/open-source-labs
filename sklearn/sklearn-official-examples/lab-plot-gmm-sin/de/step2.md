# Datensatz generieren

Als nächstes werden wir einen Datensatz generieren, der einer rauschen Sinuskurve folgt.

```python
# Parameter
n_samples = 100

# Zufällige Stichprobe generieren, die einer Sinuskurve folgt
np.random.seed(0)
X = np.zeros((n_samples, 2))
Schritt = 4.0 * np.pi / n_samples

for i in range(X.shape[0]):
    x = i * Schritt - 6.0
    X[i, 0] = x + np.random.normal(0, 0.1)
    X[i, 1] = 3.0 * (np.sin(x) + np.random.normal(0, 0.2))
```
