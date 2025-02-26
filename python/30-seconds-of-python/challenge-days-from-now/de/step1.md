# Tage ab heute

## Problem

Schreiben Sie eine Funktion `days_from_now(n)`, die eine ganze Zahl `n` als Eingabe erhält und das Datum von heute plus `n` Tagen zurückgibt.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Importieren Sie das Modul `datetime`.
2. Verwenden Sie die Methode `date.today()`, um das aktuelle Datum zu erhalten.
3. Verwenden Sie die Methode `timedelta`, um `n` Tage zum aktuellen Datum hinzuzufügen.
4. Geben Sie das neue Datum zurück.

## Beispiel

```python
>>> days_from_now(5)
datetime.date(2022, 12, 28)
>>> days_from_now(10)
datetime.date(2022, 1, 2)
```
