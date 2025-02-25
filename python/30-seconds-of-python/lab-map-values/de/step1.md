# Dictionary-Werte abbilden

Schreibe eine Funktion `map_values(obj, fn)`, die ein Dictionary `obj` und eine Funktion `fn` als Argumente nimmt und ein neues Dictionary zurückgibt, das die gleichen Schlüssel wie das ursprüngliche Dictionary hat und Werte, die durch Ausführen der bereitgestellten Funktion für jeden Wert generiert werden.

```python
def map_values(obj, fn):
  return dict((k, fn(v)) for k, v in obj.items())
```

```python
users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}
map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}
```
