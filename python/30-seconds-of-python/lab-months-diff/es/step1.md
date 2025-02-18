# Diferencia de fechas

Escribe una función llamada `months_diff(start, end)` que tome dos objetos de fecha y devuelva la diferencia en meses entre ellos. La función debe:

1. Restar `start` de `end` y utilizar `datetime.timedelta.days` para obtener la diferencia en días.
2. Dividir entre `30` y utilizar `math.ceil()` para obtener la diferencia en meses (redondeada hacia arriba).

```python
from math import ceil

def months_diff(start, end):
  return ceil((end - start).days / 30)
```

```python
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```
