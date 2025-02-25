# Establecer las fechas y generar datos aleatorios

Necesitas establecer las fechas de inicio y fin y el delta, que representa la diferencia entre cada fecha. También necesitas generar datos aleatorios para el ejemplo.

```python
date1 = datetime.date(1952, 1, 1)
date2 = datetime.date(2004, 4, 12)
delta = datetime.timedelta(days=100)

dates = drange(date1, date2, delta)
s = np.random.rand(len(dates))
```
