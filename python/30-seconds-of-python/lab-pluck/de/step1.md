# Werte aus Liste von Dictionaries extrahieren

Schreiben Sie eine Funktion `pluck(lst, key)`, die eine Liste von Dictionaries `lst` und einen Schlüssel `key` als Argumente nimmt und eine Liste der zu dem angegebenen Schlüssel `key` gehörenden Werte zurückgibt.

Sie müssen:

- Ein Listenverständnis und `dict.get()` verwenden, um den Wert von `key` für jedes Dictionary in `lst` zu erhalten.
- Die Funktion sollte eine leere Liste zurückgeben, wenn die Eingabeliste leer ist oder wenn der angegebene Schlüssel in keinem der Dictionaries vorhanden ist.

```python
def pluck(lst, key):
  return [x.get(key) for x in lst]
```

```python
simpsons = [
  { 'name': 'lisa', 'age': 8 },
  { 'name': 'homer', 'age': 36 },
  { 'name':'marge', 'age': 34 },
  { 'name': 'bart', 'age': 10 }
]
pluck(simpsons, 'age') # [8, 36, 34, 10]
```
