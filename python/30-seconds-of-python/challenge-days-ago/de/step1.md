# Herausforderung: Tage zurück

## Problem

Ihre Aufgabe ist es, eine Funktion namens `days_ago(n)` zu schreiben, die eine ganze Zahl `n` als Argument nimmt und das Datum von vor `n` Tagen ab heute zurückgibt.

Um dieses Problem zu lösen, müssen Sie die `date`-Klasse aus dem `datetime`-Modul verwenden, um das aktuelle Datum zu erhalten, und die `timedelta`-Klasse, um `n` Tage vom aktuellen Datum abzuziehen.

## Beispiel

```python
days_ago(5) # date(2022, 11, 23)
```
