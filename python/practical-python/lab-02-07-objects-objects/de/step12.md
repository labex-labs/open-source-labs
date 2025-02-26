# Übung 2.25: Erstellen von Dictionaries

Denken Sie daran, wie die `dict()`-Funktion ein Dictionary leicht erstellen kann, wenn Sie eine Sequenz von Schlüsselnamen und Werten haben? Lassen Sie uns ein Dictionary aus den Spaltenüberschriften erstellen:

```python
>>> headers
['name','shares', 'price']
>>> converted
['AA', 100, 32.2]
>>> dict(zip(headers, converted))
{'price': 32.2, 'name': 'AA','shares': 100}
>>>
```

Natürlich, wenn Sie Ihre Fähigkeiten bei der Verwendung von Listenkomprehensions beherrschen, können Sie die gesamte Umwandlung in einem Schritt mit einer Dictionary-Komprehension vornehmen:

```python
>>> { name: func(val) for name, func, val in zip(headers, types, row) }
{'price': 32.2, 'name': 'AA','shares': 100}
>>>
```
