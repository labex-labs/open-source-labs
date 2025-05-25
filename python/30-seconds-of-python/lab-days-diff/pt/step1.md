# Diferença de Datas em Dias

Escreva uma função `days_diff(start, end)` que recebe dois objetos de data como entrada e retorna o número de dias entre eles. A função deve subtrair `start` de `end` e usar `datetime.timedelta.days` para obter a diferença em dias.

```python
def days_diff(start, end):
  return (end - start).days
```

```python
from datetime import date

days_diff(date(2020, 10, 25), date(2020, 10, 28)) # 3
```
