# Datumsbereich

Schreiben Sie eine Python-Funktion namens `daterange(start, end)`, die zwei `datetime.date`-Objekte als Argumente nimmt und eine Liste aller Daten zwischen ihnen zurückgibt. Die Liste sollte das Startdatum enthalten, aber nicht das Enddatum.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `datetime.timedelta.days`, um die Anzahl der Tage zwischen `start` und `end` zu erhalten.
2. Verwenden Sie `int()`, um das Ergebnis in einen Integer zu konvertieren, und `range()`, um über jeden Tag zu iterieren.
3. Verwenden Sie eine Listenkomprehension und `datetime.timedelta`, um eine Liste von `datetime.date`-Objekten zu erstellen.

```python
from datetime import timedelta, date

def daterange(start, end):
  return [start + timedelta(n) for n in range(int((end - start).days))]
```

```python
from datetime import date

daterange(date(2020, 10, 1), date(2020, 10, 5))
# [date(2020, 10, 1), date(2020, 10, 2), date(2020, 10, 3), date(2020, 10, 4)]
```
