# Überprüfen, ob ein Datum ein Werktag ist

Schreiben Sie eine Python-Funktion namens `is_weekday()`, die ein Datum als Eingabe erhält und `True` zurückgibt, wenn es ein Werktag ist, und `False`, wenn es ein Wochenende ist. Wenn kein Datum angegeben wird, sollte die Funktion das aktuelle Datum verwenden.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Importieren Sie das Modul `datetime`.
2. Definieren Sie eine Funktion namens `is_weekday()`, die ein Datum als Eingabe erhält. Wenn kein Datum angegeben wird, verwenden Sie das aktuelle Datum.
3. Verwenden Sie die `weekday()`-Methode des `datetime`-Moduls, um den Wochentag als Ganzzahl zu erhalten. Die `weekday()`-Methode gibt eine Ganzzahl zwischen 0 (Montag) und 6 (Sonntag) zurück.
4. Überprüfen Sie, ob der Wochentag kleiner oder gleich 4 ist. Wenn ja, geben Sie `True` zurück, andernfalls geben Sie `False` zurück.

```python
from datetime import datetime

def is_weekday(d = datetime.today()):
  return d.weekday() <= 4
```

```python
from datetime import date

is_weekday(date(2020, 10, 25)) # False
is_weekday(date(2020, 10, 28)) # True
```
