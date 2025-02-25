# Desafío de Rango de Fechas

## Problema

Escribe una función de Python llamada `daterange(start, end)` que tome dos objetos `datetime.date` como argumentos y devuelva una lista de todas las fechas entre ellas. La lista debe incluir la fecha de inicio pero no la fecha final.

Para resolver este problema, puedes seguir estos pasos:

1. Utiliza `datetime.timedelta.days` para obtener el número de días entre `start` y `end`.
2. Utiliza `int()` para convertir el resultado a un entero y `range()` para iterar sobre cada día.
3. Utiliza una comprensión de lista y `datetime.timedelta` para crear una lista de objetos `datetime.date`.

## Ejemplo

```python
from datetime import date

daterange(date(2020, 10, 1), date(2020, 10, 5))
# [date(2020, 10, 1), date(2020, 10, 2), date(2020, 10, 3), date(2020, 10, 4)]
```
