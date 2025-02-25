# Erstelle Daten

In diesem Schritt erstellen wir ein Dictionary `data`, das Werte für die Variablen `a`, `b`, `c` und `d` enthält.

```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
```
