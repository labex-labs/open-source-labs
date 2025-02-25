# Schlüssel mit Wert finden

## Problem

Schreiben Sie eine Python-Funktion namens `find_keys(dictionary, value)`, die ein Dictionary und einen Wert als Argumente übernimmt und eine Liste aller Schlüssel im Dictionary zurückgibt, die den angegebenen Wert haben. Wenn es keine Schlüssel mit dem angegebenen Wert gibt, sollte die Funktion eine leere Liste zurückgeben.

Um dieses Problem zu lösen, können Sie die `dictionary.items()`-Methode verwenden, die einen Generator zurückgibt, der Schlüssel-Wert-Paare des Dictionaries liefert. Anschließend können Sie eine Listenkomprehension verwenden, um die Schlüssel zu filtern, die den angegebenen Wert haben.

## Beispiel

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
find_keys(ages, 10) # [ 'Peter', 'Anna' ]
```

In diesem Beispiel wird die `find_keys()`-Funktion mit einem Dictionary `ages` und einem Wert `10` aufgerufen. Die Funktion gibt eine Liste von Schlüsseln zurück, die den Wert `10` haben, nämlich `'Peter'` und `'Anna'`.
