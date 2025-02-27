# Datensatz laden und vorbereiten

Wir laden den Digits-Datensatz und bereiten ihn für das Clustering vor, indem wir die Daten und die Ziel-Labels extrahieren. Wir setzen auch den Zufallszahlengenerator auf Null, um die Reproduzierbarkeit zu gewährleisten.

```python
digits = datasets.load_digits()
X, y = digits.data, digits.target
n_samples, n_features = X.shape
np.random.seed(0)
```
