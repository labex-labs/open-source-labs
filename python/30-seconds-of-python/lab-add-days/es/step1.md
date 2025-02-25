# Añadir días a una fecha

Escribe una función `add_days(n, d)` que tome dos argumentos:

- `n`: un entero que representa el número de días a sumar (si es positivo) o restar (si es negativo) a la fecha dada.
- `d`: un argumento opcional que representa la fecha a la que se deben sumar o restar los días. Si no se proporciona, se debe utilizar la fecha actual.

La función debe devolver un objeto `datetime` que representa la nueva fecha después de sumar o restar el número especificado de días.

```python
from datetime import datetime, timedelta

def add_days(n, d = datetime.today()):
  return d + timedelta(n)
```

```python
from datetime import date

add_days(5, date(2020, 10, 25)) # date(2020, 10, 30)
add_days(-5, date(2020, 10, 25)) # date(2020, 10, 20)
```
