# Convert numpy.datetime64 to matplotlib date

`numpy.datetime64` objects have microsecond precision for a much larger timespace than `.datetime` objects. However, currently, Matplotlib time is only converted back to datetime objects, which have microsecond resolution and years that only span 0000 to 9999.

```python
date1 = np.datetime64('2000-01-01T00:10:00.000012')
mdate1 = mdates.date2num(date1)
```
