# Convertir datetime a fecha de Matplotlib

Ahora que se ha establecido la época, podemos convertir un objeto `datetime` a una fecha de Matplotlib utilizando la función `mdates.date2num`.

```python
date1 = datetime.datetime(2000, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
