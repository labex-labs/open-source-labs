# Dictionary-Schlüssel

## Problem

Schreiben Sie eine Funktion `keys_only(flat_dict)`, die ein flaches Dictionary als Eingabe nimmt und eine Liste aller seiner Schlüssel zurückgibt.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `dict.keys()`, um die Schlüssel im gegebenen Dictionary zurückzugeben.
2. Geben Sie eine `list()` des vorherigen Ergebnisses zurück.

## Beispiel

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
keys_only(ages) # ['Peter', 'Isabel', 'Anna']
```
