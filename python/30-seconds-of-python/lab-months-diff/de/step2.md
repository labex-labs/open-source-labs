# Erstellen der Funktion zur Monatsdifferenzberechnung

Nachdem wir nun verstehen, wie man mit Datumsobjekten arbeitet und die Differenz in Tagen berechnet, erstellen wir eine Funktion zur Berechnung der Differenz in Monaten.

In vielen Anwendungen wird ein Monat auf 30 Tage approximiert. Obwohl dies nicht immer genau ist (Monate können zwischen 28 und 31 Tage haben), ist es eine gängige Vereinfachung, die für viele Geschäftsberechnungen gut funktioniert.

Öffnen Sie Ihre `month_difference.py`-Datei und fügen Sie diese Funktion unterhalb Ihres bestehenden Codes hinzu:

```python
def months_diff(start, end):
    """
    Calculate the difference in months between two dates.

    Args:
        start (date): The start date
        end (date): The end date

    Returns:
        int: The number of months between the dates (rounded up)
    """
    # Calculate the difference in days
    days_difference = (end - start).days

    # Convert days to months (assuming 30 days per month) and round up
    months = ceil(days_difference / 30)

    return months
```

Lassen Sie uns verstehen, was diese Funktion tut:

1. Sie nimmt zwei Parameter entgegen: `start` und `end`, die Datumsobjekte sind.
2. Sie berechnet die Differenz in Tagen zwischen diesen Daten.
3. Sie teilt durch 30, um die Tage in Monate umzurechnen.
4. Sie verwendet `ceil()`, um auf die nächste ganze Zahl aufzurunden.
5. Sie gibt das Ergebnis als Ganzzahl zurück.

Die `ceil()`-Funktion wird verwendet, weil in vielen Geschäftsszenarien auch ein Teilmonat aus Abrechnungsgründen als ganzer Monat gezählt wird.

Um unsere Funktion zu testen, fügen Sie folgenden Code am Ende Ihrer Datei hinzu:

```python
# Test the months_diff function with our example dates
print(f"Months between {date1} and {date2}: {months_diff(date1, date2)}")

# Test with some other date pairs
print(f"Months between 2020-10-28 and 2020-11-25: {months_diff(date(2020, 10, 28), date(2020, 11, 25))}")
print(f"Months between 2020-12-15 and 2021-01-10: {months_diff(date(2020, 12, 15), date(2021, 01, 10))}")
```

Speichern Sie Ihre Datei und führen Sie sie erneut aus:

```bash
python3 ~/project/month_difference.py
```

Sie sollten eine Ausgabe wie die folgende sehen:

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
Months between 2023-01-15 and 2023-03-20: 3
Months between 2020-10-28 and 2020-11-25: 1
Months between 2020-12-15 and 2021-01-10: 1
```

Beachten Sie, dass:

- Die 64 Tage zwischen dem 15. Januar 2023 und dem 20. März 2023 werden als 3 Monate berechnet (64/30 = 2,13, auf 3 aufgerundet).
- Die Differenz zwischen dem 28. Oktober und dem 25. November wird als 1 Monat berechnet.
- Die Differenz zwischen dem 15. Dezember und dem 10. Januar (über ein Jahresende hinweg) wird ebenfalls als 1 Monat berechnet.
