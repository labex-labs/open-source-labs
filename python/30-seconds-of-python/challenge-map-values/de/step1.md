# Dictionary-Werte abbilden

## Problem

Schreiben Sie eine Funktion `map_values(obj, fn)`, die ein Dictionary `obj` und eine Funktion `fn` als Argumente nimmt und ein neues Dictionary zurückgibt, das die gleichen Schlüssel wie das ursprüngliche Dictionary hat und Werte, die durch Ausführen der bereitgestellten Funktion für jeden Wert generiert werden.

## Beispiel

```python
users = {
  'fred': { 'user': 'fred', 'age': 40 },
  'pebbles': { 'user': 'pebbles', 'age': 1 }
}
map_values(users, lambda u : u['age']) # {'fred': 40, 'pebbles': 1}
```

## Einschränkungen

- Die Funktion sollte für jedes Dictionary und jede Funktion funktionieren, die die Anforderungen erfüllen.
- Die Funktion sollte das ursprüngliche Dictionary nicht modifizieren.
