# Diferencia de fechas en días

## Problema

Escribe una función `days_diff(start, end)` que tome dos objetos de fecha como entrada y devuelva el número de días entre ellas. La función debe restar `start` de `end` y utilizar `datetime.timedelta.days` para obtener la diferencia de días.

## Ejemplo

```python
from datetime import date

assert days_diff(date(2020, 10, 25), date(2020, 10, 28)) == 3
assert days_diff(date(2021, 1, 1), date(2021, 1, 1)) == 0
assert days_diff(date(2021, 1, 1), date(2021, 1, 2)) == 1
```
