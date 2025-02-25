# Konvertieren von datetime in Matplotlib-Datum

Jetzt, nachdem die Epoche festgelegt wurde, können wir ein `datetime`-Objekt in ein Matplotlib-Datum mit der Funktion `mdates.date2num` umwandeln.

```python
date1 = datetime.datetime(2000, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
