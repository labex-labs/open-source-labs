# Erstellen eines Rekordarrays

Ein Rekordarray ist eine Unterklasse von ndarray, die den Zugang zu Feldern über Attribute statt über Indizes ermöglicht. Wir können ein Rekordarray mit der Funktion `np.rec.array` erstellen.

```python
# Erstellen eines Rekordarrays
recordarr = np.rec.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
