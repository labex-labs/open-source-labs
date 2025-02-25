# Das geschachtelte Element abrufen

Schreiben Sie eine Funktion `get(d, selectors)`, die ein Wörterbuch oder eine Liste `d` und eine Liste von Selektoren `selectors` als Argumente übernimmt und den Wert des geschachtelten Schlüssels zurückgibt, der durch die gegebene Selektorenliste angegeben wird. Wenn der Schlüssel nicht existiert, geben Sie `None` zurück.

Um diese Funktion zu implementieren, verwenden Sie `functools.reduce()`, um über die `selectors`-Liste zu iterieren. Wenden Sie `operator.getitem()` auf jeden Schlüssel in `selectors` an, um den Wert abzurufen, der als Iterand für die nächste Iteration verwendet werden soll.

```python
from functools import reduce
from operator import getitem

def get(d, selectors):
  return reduce(getitem, selectors, d)
```

```python
users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last': 'smith'
    },
    'postIds': [1, 2, 3]
  }
}
get(users, ['freddy', 'name', 'last']) # 'smith'
get(users, ['freddy', 'postIds', 1]) # 2
```
