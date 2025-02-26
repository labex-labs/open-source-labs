# Wachstum von Wörterbüchern/Klassen

Python-Wörterbücher (und Klassen) erlauben es, bis zu 5 Werte zu speichern, bevor ihr reservierter Arbeitsspeicher verdoppelt wird. Untersuchen Sie dies, indem Sie ein Wörterbuch erstellen und einige weitere Werte hinzufügen:

```python
>>> row = { 'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354 }
>>> sys.getsizeof(row)
>>> sys.getsizeof(row)
240
>>> row['a'] = 1
>>> sys.getsizeof(row)
240
>>> row['b'] = 2
>>> sys.getsizeof(row)
368
>>>
```

Geht der Arbeitsspeicher zurück, wenn Sie das gerade hinzugefügte Element löschen?

Nahrung für die Gedanken: Wenn Sie eine große Anzahl von Datensätzen erstellen, kann die Darstellung jedes Datensatzes als Wörterbuch nicht der effizienteste Ansatz sein - Sie könnten einen hohen Preis für die Bequemlichkeit eines Wörterbuchs zahlen. Es might besser sein, die Verwendung von Tupeln, benannten Tupeln oder Klassen zu erwägen, die `__slots__` definieren.
