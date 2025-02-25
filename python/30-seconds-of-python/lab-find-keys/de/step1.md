# Schlüssel mit einem bestimmten Wert finden

Schreiben Sie eine Python-Funktion namens `find_keys(dictionary, value)`, die ein Wörterbuch und einen Wert als Argumente übernimmt und eine Liste aller Schlüssel im Wörterbuch zurückgibt, die den angegebenen Wert haben. Wenn es keine Schlüssel mit dem angegebenen Wert gibt, sollte die Funktion eine leere Liste zurückgeben.

Um dieses Problem zu lösen, können Sie die `dictionary.items()`-Methode verwenden, die einen Generator zurückgibt, der Schlüssel-Wert-Paare des Wörterbuchs liefert. Anschließend können Sie eine Listenkomprehension verwenden, um die Schlüssel zu filtern, die den angegebenen Wert haben.

```python
def find_keys(dict, val):
  return list(key for key, value in dict.items() if value == val)
```

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
find_keys(ages, 10) # [ 'Peter', 'Anna' ]
```
