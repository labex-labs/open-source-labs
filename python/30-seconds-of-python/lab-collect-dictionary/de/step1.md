# Ein Dictionary umkehren

Schreiben Sie eine Funktion `invert_dictionary(obj)`, die ein Dictionary `obj` als Eingabe nimmt und ein neues Dictionary zurückgibt, bei dem die Schlüssel und Werte vertauscht sind. Das Eingabedictionary wird nicht-eindeutige hashbare Werte haben. Wenn zwei oder mehr Schlüssel den gleichen Wert haben, sollte die Funktion die Schlüssel in einer Liste im Ausgabedictionary anhängen.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Erstellen Sie ein `collections.defaultdict` mit `list` als Standardwert für jeden Schlüssel.
2. Verwenden Sie `dictionary.items()` in Kombination mit einer Schleife, um die Werte des Dictionaries mithilfe von `dict.append()` zu Schlüsseln zuzuordnen.
3. Verwenden Sie `dict()`, um das `collections.defaultdict` in ein reguläres Dictionary umzuwandeln.

Funktionssignatur: `def invert_dictionary(obj: dict) -> dict:`

```python
from collections import defaultdict

def collect_dictionary(obj):
  inv_obj = defaultdict(list)
  for key, value in obj.items():
    inv_obj[value].append(key)
  return dict(inv_obj)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}
collect_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```
