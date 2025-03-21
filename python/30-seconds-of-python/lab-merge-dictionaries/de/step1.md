# Wörterbücher zusammenführen

Schreiben Sie eine Funktion `merge_dictionaries(*dicts)`, die zwei oder mehr Wörterbücher als Argumente annimmt und ein neues Wörterbuch zurückgibt, das alle Schlüssel-Wert-Paare aus den Eingabewörterbüchern enthält.

Ihre Funktion sollte ein neues Wörterbuch erstellen und über die Eingabewörterbücher iterieren, wobei `dictionary.update()` verwendet wird, um die Schlüssel-Wert-Paare aus jedem einzufügen.

```python
def merge_dictionaries(*dicts):
  res = dict()
  for d in dicts:
    res.update(d)
  return res
```

```python
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```
