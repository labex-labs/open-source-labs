# Tage ab heute

Schreiben Sie eine Funktion `days_from_now(n)`, die eine ganze Zahl `n` als Eingabe erhält und das Datum von heute aus in `n` Tagen zurückgibt.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Importieren Sie das Modul `datetime`.
2. Verwenden Sie die Methode `date.today()`, um das aktuelle Datum zu erhalten.
3. Verwenden Sie die Methode `timedelta`, um `n` Tage zum aktuellen Datum hinzuzufügen.
4. Geben Sie das neue Datum zurück.

```python
from datetime import timedelta, date

def days_from_now(n):
  return date.today() + timedelta(n)
```

```python
days_from_now(5) # date(2020, 11, 02)
```
