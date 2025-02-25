# Den Schlüssel eines Werts in einem Wörterbuch finden

## Problemstellung

Schreiben Sie eine Funktion `find_key(dict, val)`, die den ersten Schlüssel im bereitgestellten Wörterbuch findet, der den angegebenen Wert hat.

Ihre Funktion sollte:

- Ein Wörterbuch `dict` und einen Wert `val` als Eingabe entgegennehmen.
- `dictionary.items()` und `next()` verwenden, um den ersten Schlüssel zurückzugeben, dessen Wert gleich `val` ist.
- Den Schlüssel als Ausgabe zurückgeben.

## Beispiel

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
find_key(ages, 11) # 'Isabel'
```
