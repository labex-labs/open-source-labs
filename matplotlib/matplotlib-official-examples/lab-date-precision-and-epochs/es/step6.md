# Convertir datetime a fecha de Matplotlib con la nueva época

Ahora que se ha establecido la época al nuevo valor predeterminado, podemos convertir un objeto `datetime` a una fecha de Matplotlib utilizando la función `mdates.date2num`.

```python
date1 = datetime.datetime(2020, 1, 1, 0, 10, 0, 12, tzinfo=datetime.timezone.utc)
mdate1 = mdates.date2num(date1)
```
