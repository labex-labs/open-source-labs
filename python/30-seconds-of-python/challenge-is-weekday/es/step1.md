# Comprueba si una fecha es un día hábil

## Problema

Escribe una función de Python llamada `is_weekday()` que tome una fecha como entrada y devuelva `True` si es un día hábil y `False` si es un fin de semana. Si no se proporciona ninguna fecha, la función debe usar la fecha actual.

Para resolver este problema, puedes seguir estos pasos:

1. Importa el módulo `datetime`.
2. Define una función llamada `is_weekday()` que tome una fecha como entrada. Si no se proporciona ninguna fecha, utiliza la fecha actual.
3. Utiliza el método `weekday()` del módulo `datetime` para obtener el día de la semana como un entero. El método `weekday()` devuelve un entero entre 0 (lunes) y 6 (domingo).
4. Comprueba si el día de la semana es menor o igual a 4. Si es así, devuelve `True`, de lo contrario devuelve `False`.

## Ejemplo

Aquí hay algunos ejemplos de cómo debe comportarse tu función:

```python
from datetime import date

assert is_weekday(date(2022, 11, 11)) == False
assert is_weekday(date(2022, 11, 14)) == True
assert is_weekday(date(2022, 11, 12)) == False
assert is_weekday(date(2022, 11, 13)) == False
```
