# Konvertieren von numpy.datetime64 in Matplotlib-Datum

`numpy.datetime64`-Objekte haben eine Mikrosekundengenauigkeit für einen viel größeren Zeitraum als `.datetime`-Objekte. Allerdings wird derzeit die Matplotlib-Zeit nur in `datetime`-Objekte zurückkonvertiert, die eine Mikrosekundenauflösung haben und Jahre, die nur von 0000 bis 9999 reichen.

```python
date1 = np.datetime64('2000-01-01T00:10:00.000012')
mdate1 = mdates.date2num(date1)
```
