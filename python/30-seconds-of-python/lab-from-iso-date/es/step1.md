# Convertir fecha ISO

Escribe una función `from_iso_date(d)` que tome una cadena `d` que representa una fecha en formato ISO-8601 y devuelva un objeto `datetime.datetime` que representa la misma fecha y hora.

```python
from datetime import datetime

def from_iso_date(d):
  return datetime.fromisoformat(d)
```

```python
from_iso_date('2020-10-28T12:30:59.000000') # 2020-10-28 12:30:59
```
