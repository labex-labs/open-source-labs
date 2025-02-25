# La fecha es fin de semana

Escribe una función `is_weekend(d)` que tome un objeto de fecha como entrada y devuelva `True` si la fecha dada es un fin de semana, y `False` en caso contrario. Si no se proporciona ningún argumento, la función debe utilizar la fecha actual.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza el método `datetime.datetime.weekday()` para obtener el día de la semana como un entero.
2. Comprueba si el día de la semana es mayor que `4`. Si es así, devuelve `True`, de lo contrario devuelve `False`.

```python
from datetime import datetime

def is_weekend(d = datetime.today()):
  return d.weekday() > 4
```

```python
from datetime import date

is_weekend(date(2020, 10, 25)) # True
is_weekend(date(2020, 10, 28)) # False
```
