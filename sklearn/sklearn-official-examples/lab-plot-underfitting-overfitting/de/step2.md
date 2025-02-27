# Daten generieren

Wir werden 30 Stichproben aus einer Kosinusfunktion generieren und den Stichproben zufälliger Rauschen hinzufügen.

```python
def true_fun(X):
    return np.cos(1.5 * np.pi * X)

np.random.seed(0)

n_samples = 30

X = np.sort(np.random.rand(n_samples))
y = true_fun(X) + np.random.randn(n_samples) * 0.1
```