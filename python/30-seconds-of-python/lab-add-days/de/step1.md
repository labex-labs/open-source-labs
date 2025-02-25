# Tagen zum Datum hinzufügen

Schreiben Sie eine Funktion `add_days(n, d)`, die zwei Argumente annimmt:

- `n`: eine Ganzzahl, die die Anzahl der Tage angibt, die hinzugefügt (wenn positiv) oder subtrahiert (wenn negativ) werden sollen, von dem angegebenen Datum.
- `d`: ein optionales Argument, das das Datum angibt, zu dem die Tage hinzugefügt oder subtrahiert werden sollen. Wenn nicht angegeben, sollte das aktuelle Datum verwendet werden.

Die Funktion sollte ein `datetime`-Objekt zurückgeben, das das neue Datum darstellt, nachdem die angegebene Anzahl von Tagen hinzugefügt oder subtrahiert wurde.

```python
from datetime import datetime, timedelta

def add_days(n, d = datetime.today()):
  return d + timedelta(n)
```

```python
from datetime import date

add_days(5, date(2020, 10, 25)) # date(2020, 10, 30)
add_days(-5, date(2020, 10, 25)) # date(2020, 10, 20)
```
