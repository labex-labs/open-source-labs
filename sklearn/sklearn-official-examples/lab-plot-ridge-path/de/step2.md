# Daten generieren

In diesem Schritt werden wir eine 10x10-Hilbert-Matrix generieren und die Zielfunktion y als Vektor aus Einsen festlegen.

```python
X = 1.0 / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)
```
