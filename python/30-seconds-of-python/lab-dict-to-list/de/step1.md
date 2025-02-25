# Dictionary in Liste

Schreiben Sie eine Funktion `dict_to_list(d)`, die ein Dictionary `d` als Argument nimmt und eine Liste von Tupeln zurückgibt. Jedes Tupel sollte ein Schlüssel-Wert-Paar aus dem Dictionary enthalten. Die Reihenfolge der Tupel in der Liste sollte dieselbe sein wie die Reihenfolge der Schlüssel-Wert-Paare im Dictionary.

```python
def dict_to_list(d):
  return list(d.items())
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
dict_to_list(d)
# [('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)]
```
