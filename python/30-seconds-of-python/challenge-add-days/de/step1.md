# Füge Tagen zu einem Datum hinzu

## Problemstellung

Schreiben Sie eine Funktion `add_days(n, d)`, die zwei Argumente annimmt:

- `n`: eine Ganzzahl, die die Anzahl der Tage angibt, die hinzugefügt (wenn positiv) oder subtrahiert (wenn negativ) werden sollen, von dem angegebenen Datum.
- `d`: ein optionales Argument, das das Datum angibt, zu dem die Tage hinzugefügt oder subtrahiert werden sollen. Wenn nicht angegeben, sollte das aktuelle Datum verwendet werden.

Die Funktion sollte ein `datetime`-Objekt zurückgeben, das das neue Datum darstellt, nachdem die angegebene Anzahl von Tagen hinzugefügt oder subtrahiert wurde.

## Beispiel

```python
from datetime import date

add_days(5, date(2020, 10, 25)) # gibt datetime.date(2020, 10, 30) zurück
add_days(-5, date(2020, 10, 25)) # gibt datetime.date(2020, 10, 20) zurück
```
