# Konvertieren von datetime in Matplotlib-Datum mit neuer Epoche

Jetzt, nachdem die Epoche auf die neue Standardeinstellung gesetzt wurde, können wir ein `datetime`-Objekt in ein Matplotlib-Datum mit der Funktion `mdates.date2num` umwandeln.

```python
date1 = datetime.datetime(2020, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
