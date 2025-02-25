# Setze die Daten und generiere zufällige Daten

Du musst das Start- und Enddatum sowie den Zeitintervall (Delta) setzen, der die Differenz zwischen jedem Datum darstellt. Du musst auch für das Beispiel zufällige Daten generieren.

```python
date1 = datetime.date(1952, 1, 1)
date2 = datetime.date(2004, 4, 12)
delta = datetime.timedelta(days=100)

dates = drange(date1, date2, delta)
s = np.random.rand(len(dates))
```
