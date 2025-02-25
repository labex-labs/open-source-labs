# Diferencia de fechas en días

Escribe una función `days_diff(start, end)` que tome dos objetos de fecha como entrada y devuelva el número de días entre ellas. La función debe restar `start` de `end` y utilizar `datetime.timedelta.days` para obtener la diferencia de días.

```python
def days_diff(start, end):
  return (end - start).days
```

```python
from datetime import date

days_diff(date(2020, 10, 25), date(2020, 10, 28)) # 3
```
