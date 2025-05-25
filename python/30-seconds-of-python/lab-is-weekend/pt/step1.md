# Data é Fim de Semana

Escreva uma função `is_weekend(d)` que recebe um objeto de data como entrada e retorna `True` se a data fornecida for um fim de semana, e `False` caso contrário. Se nenhum argumento for fornecido, a função deve usar a data atual.

Para resolver este problema, você pode seguir estes passos:

1. Use o método `datetime.datetime.weekday()` para obter o dia da semana como um inteiro.
2. Verifique se o dia da semana é maior que `4`. Se for, retorne `True`, caso contrário, retorne `False`.

```python
from datetime import datetime

def is_weekend(d = datetime.today()):
  return d.weekday() > 4
```

```python
from datetime import date

is_weekend(date(2020, 10, 25)) # True
is_weekend(date(2020, 10, 28)) # False
```
