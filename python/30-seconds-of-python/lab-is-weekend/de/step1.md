# Datum ist Wochenende

Schreiben Sie eine Funktion `is_weekend(d)`, die ein Datumsobjekt als Eingabe erhält und `True` zurückgibt, wenn das gegebene Datum ein Wochenende ist, und `False` sonst. Wenn kein Argument angegeben wird, sollte die Funktion das aktuelle Datum verwenden.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie die Methode `datetime.datetime.weekday()`, um den Wochentag als Ganzzahl zu erhalten.
2. Überprüfen Sie, ob der Wochentag größer als `4` ist. Wenn ja, geben Sie `True` zurück, andernfalls `False`.

```python
from datetime import datetime

def is_weekend(d = datetime.today()):
  return d.weekday() > 4
```

```python
from datetime import date

is_weekend(date(2020, 10, 25)) # True
is_weekend(date(2020, 10, 28)) # False
```
