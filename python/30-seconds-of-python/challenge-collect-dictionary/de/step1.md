# Ein Wörterbuch umkehren

## Problem

Schreiben Sie eine Funktion `invert_dictionary(obj)`, die ein Wörterbuch `obj` als Eingabe nimmt und ein neues Wörterbuch zurückgibt, bei dem die Schlüssel und Werte vertauscht sind. Das Eingabewörterbuch wird nicht eindeutige hashbare Werte haben. Wenn zwei oder mehr Schlüssel den gleichen Wert haben, sollte die Funktion die Schlüssel in einer Liste im Ausgabewörterbuch anhängen.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Erstellen Sie ein `collections.defaultdict` mit `list` als Standardwert für jeden Schlüssel.
2. Verwenden Sie `dictionary.items()` in Kombination mit einer Schleife, um die Werte des Wörterbuchs mithilfe von `dict.append()` zu Schlüsseln zuzuordnen.
3. Verwenden Sie `dict()`, um das `collections.defaultdict` in ein reguläres Wörterbuch zu konvertieren.

Funktionssignatur: `def invert_dictionary(obj: dict) -> dict:`

## Beispiel

```python
ages = {
  'Peter': 10,
  'Isabel': 10,
  'Anna': 9,
}
invert_dictionary(ages) # { 10: ['Peter', 'Isabel'], 9: ['Anna'] }
```
