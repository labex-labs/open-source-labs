# Data para formato ISO

Escreva uma função `to_iso_date(d)` que recebe um objeto `datetime.datetime` como argumento e retorna uma string representando a data no formato ISO-8601. A função deve usar o método `datetime.datetime.isoformat()` para converter a data para sua representação ISO-8601.

```python
from datetime import datetime

def to_iso_date(d):
  return d.isoformat()
```

```python
from datetime import datetime

to_iso_date(datetime(2020, 10, 25)) # 2020-10-25T00:00:00
```
