# Fecha al formato ISO

## Problema

Escribe una función `to_iso_date(d)` que tome un objeto `datetime.datetime` como argumento y devuelva una cadena que represente la fecha en formato ISO-8601. La función debe utilizar el método `datetime.datetime.isoformat()` para convertir la fecha a su representación ISO-8601.

## Ejemplo

```python
from datetime import datetime

to_iso_date(datetime(2020, 10, 25)) # "2020-10-25T00:00:00"
```
