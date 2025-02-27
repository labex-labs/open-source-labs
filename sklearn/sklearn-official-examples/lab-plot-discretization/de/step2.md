# Erstellen des Datensatzes

In diesem Schritt erstellen wir einen Datensatz mit einem kontinuierlichen Eingangsmerkmal und einem kontinuierlichen Ausgangsmerkmal. Wir werden die `numpy.random.RandomState()`-Methode verwenden, um Zufallszahlen für das Eingangsmerkmal zu generieren, und die `numpy.sin()`-Methode, um das Ausgangsmerkmal zu generieren.

```python
rnd = np.random.RandomState(42)
X = rnd.uniform(-3, 3, size=100)
y = np.sin(X) + rnd.normal(size=len(X)) / 3
X = X.reshape(-1, 1)
```
