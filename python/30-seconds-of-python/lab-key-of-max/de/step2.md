# Behandlung des Falls eines leeren Wörterbuchs

Unsere aktuelle Funktion hat ein Problem: Sie stürzt ab, wenn das Eingabewörterbuch `d` leer ist. Lassen Sie uns das beheben. Ändern Sie die Datei `key_of_max.py` so, dass sie wie folgt aussieht:

```python
def key_of_max(d):
  """
  Gibt den Schlüssel zurück, der dem maximalen Wert im Wörterbuch 'd' zugeordnet ist.

  Wenn mehrere Schlüssel denselben maximalen Wert haben, kann einer beliebiger von ihnen zurückgegeben werden.
  """
  if not d:  # Check if the dictionary is empty
      return None
  return max(d, key=d.get)
```

Die hinzugefügten Zeilen tun Folgendes:

- **`if not d:`**: In Python wird ein leeres Wörterbuch als "falsch" (falsy) angesehen. Diese `if`-Anweisung prüft, ob das Wörterbuch `d` leer ist.
- **`return None`**: Wenn das Wörterbuch leer ist, gibt es keinen maximalen Wert. Daher geben wir `None` zurück. Dies ist eine Standardmethode, um das Fehlen eines Werts in Python anzuzeigen. Dadurch wird verhindert, dass die `max()`-Funktion einen Fehler auslöst.

Dies ist ein entscheidender Schritt beim Schreiben robuster Code: Berücksichtigen Sie immer Randfälle!
