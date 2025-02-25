# Daten erstellen

In diesem Schritt werden wir die Daten für unseren Graphen erstellen. Wir werden ein Array von Werten für t und ein Array von Werten für s erstellen.

```python
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)
```
