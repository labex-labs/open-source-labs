# Días atrás

Tu tarea es escribir una función llamada `days_ago(n)` que tome un entero `n` como argumento y devuelva la fecha de hace `n` días a partir de hoy.

Para resolver este problema, debes usar la clase `date` del módulo `datetime` para obtener la fecha actual y la clase `timedelta` para restar `n` días a la fecha actual.

```python
from datetime import timedelta, date

def days_ago(n):
  return date.today() - timedelta(n)
```

```python
days_ago(5) # date(2020, 10, 23)
```
