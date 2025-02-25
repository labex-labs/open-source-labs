# Den Schlüssel eines Werts in einem Dictionary finden

Schreiben Sie eine Funktion `find_key(dict, val)`, die den ersten Schlüssel im bereitgestellten Dictionary findet, der den angegebenen Wert hat.

Ihre Funktion sollte:

- Ein Dictionary `dict` und einen Wert `val` als Eingabe entgegennehmen.
- `dictionary.items()` und `next()` verwenden, um den ersten Schlüssel zurückzugeben, dessen Wert gleich `val` ist.
- Den Schlüssel als Ausgabe zurückgeben.

```python
def find_key(dict, val):
  return next(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
find_key(ages, 11) # 'Isabel'
```
