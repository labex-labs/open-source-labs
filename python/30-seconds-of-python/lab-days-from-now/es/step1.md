# Días a partir de ahora

Escribe una función `days_from_now(n)` que tome un entero `n` como entrada y devuelva la fecha de `n` días a partir de hoy.

Para resolver este problema, puedes seguir estos pasos:

1. Importa el módulo `datetime`.
2. Utiliza el método `date.today()` para obtener la fecha actual.
3. Utiliza el método `timedelta` para sumar `n` días a la fecha actual.
4. Devuelve la nueva fecha.

```python
from datetime import timedelta, date

def days_from_now(n):
  return date.today() + timedelta(n)
```

```python
days_from_now(5) # date(2020, 11, 02)
```
