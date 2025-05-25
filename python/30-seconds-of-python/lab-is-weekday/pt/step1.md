# Verificar se uma Data é um Dia de Semana

Escreva uma função Python chamada `is_weekday()` que recebe uma data como entrada e retorna `True` se for um dia de semana e `False` se for um fim de semana. Se nenhuma data for fornecida, a função deve usar a data atual.

Para resolver este problema, você pode seguir estes passos:

1. Importe o módulo `datetime`.
2. Defina uma função chamada `is_weekday()` que recebe uma data como entrada. Se nenhuma data for fornecida, use a data atual.
3. Use o método `weekday()` do módulo `datetime` para obter o dia da semana como um inteiro. O método `weekday()` retorna um inteiro entre 0 (segunda-feira) e 6 (domingo).
4. Verifique se o dia da semana é menor ou igual a 4. Se for, retorne `True`, caso contrário, retorne `False`.

```python
from datetime import datetime

def is_weekday(d = datetime.today()):
  return d.weekday() <= 4
```

```python
from datetime import date

is_weekday(date(2020, 10, 25)) # False
is_weekday(date(2020, 10, 28)) # True
```
