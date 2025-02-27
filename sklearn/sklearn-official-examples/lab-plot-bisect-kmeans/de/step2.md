# Beispiel-Daten generieren

In diesem Schritt werden wir Beispiel-Daten mit der Funktion `make_blobs()` aus scikit-learn generieren. Wir werden 10000 Proben mit 2 Zentren generieren.

```python
n_samples = 10000
random_state = 0
X, _ = make_blobs(n_samples=n_samples, centers=2, random_state=random_state)
```
