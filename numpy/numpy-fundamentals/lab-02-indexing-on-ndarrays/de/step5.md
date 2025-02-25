# Zugang zu Feldern

Wenn das ndarray-Objekt ein strukturiertes Array ist, können die Felder des Arrays durch Indexieren des Arrays mit Strings, ähnlich einem Dictionary, zugegriffen werden.

```python
x = np.array([(1, 2), (3, 4), (5, 6)], dtype=[('a', np.int32), ('b', np.int32)])
print(x['a'])  # Ausgabe: [1, 3, 5]
```
