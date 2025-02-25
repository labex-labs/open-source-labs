# La fecha es fin de semana

## Problema

Escribe una función `is_weekend(d)` que tome un objeto de fecha como entrada y devuelva `True` si la fecha dada es un fin de semana, y `False` en caso contrario. Si no se proporciona ningún argumento, la función debe utilizar la fecha actual.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza el método `datetime.datetime.weekday()` para obtener el día de la semana como un número entero.
2. Comprueba si el día de la semana es mayor que `4`. Si es así, devuelve `True`, de lo contrario devuelve `False`.

## Ejemplo

```python
from datetime import date

assert is_weekend(date(2022, 1, 1)) == True
assert is_weekend(date(2022, 1, 3)) == False
assert is_weekend() == False # la fecha actual no es un fin de semana
```
