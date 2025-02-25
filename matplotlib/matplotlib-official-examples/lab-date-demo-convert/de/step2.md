# Definieren der Daten und des Zeitintervalls

Als nächstes werden wir die Daten und die Zeitintervalle mit der datetime-Bibliothek definieren. Der Zeitraum soll vom 2. März 2000 bis zum 6. März 2000 mit einem Intervall von 6 Stunden betragen. Kopieren und einfügen Sie den folgenden Code:

```python
date1 = datetime.datetime(2000, 3, 2)
date2 = datetime.datetime(2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)
```
