# Converter Data ISO

Escreva uma função `from_iso_date(d)` que recebe uma string `d` representando uma data no formato ISO-8601 e retorna um objeto `datetime.datetime` representando a mesma data e hora.

```python
from datetime import datetime

def from_iso_date(d):
  return datetime.fromisoformat(d)
```

```python
from_iso_date('2020-10-28T12:30:59.000000') # 2020-10-28 12:30:59
```
