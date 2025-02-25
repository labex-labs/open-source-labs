# Umkehrung des Datums mit neuer Epoche

Wir können dann das Datum in die ursprüngliche Richtung zurückverfolgen, indem wir die Funktion `mdates.num2date` verwenden, um sicherzustellen, dass die Umwandlung korrekt ist.

```python
date2 = mdates.num2date(mdate1)
```
