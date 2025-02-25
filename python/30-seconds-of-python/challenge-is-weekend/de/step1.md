# Datum ist Wochenende

## Problem

Schreiben Sie eine Funktion `is_weekend(d)`, die ein Datumsobjekt als Eingabe erhält und `True` zurückgibt, wenn das gegebene Datum ein Wochenende ist, und `False` andernfalls. Wenn kein Argument angegeben wird, soll die Funktion das aktuelle Datum verwenden.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie die Methode `datetime.datetime.weekday()`, um den Wochentag als Ganzzahl zu erhalten.
2. Überprüfen Sie, ob der Wochentag größer als `4` ist. Wenn ja, geben Sie `True` zurück, andernfalls `False`.

## Beispiel

```python
from datetime import date

assert is_weekend(date(2022, 1, 1)) == True
assert is_weekend(date(2022, 1, 3)) == False
assert is_weekend() == False # aktuelles Datum ist kein Wochenende
```
