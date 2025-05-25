# Intervalo de Datas (Date Range)

Escreva uma função Python chamada `daterange(start, end)` que recebe dois objetos `datetime.date` como argumentos e retorna uma lista de todas as datas entre eles. A lista deve incluir a data de início, mas não a data de término.

Para resolver este problema, você pode seguir estes passos:

1. Use `datetime.timedelta.days` para obter o número de dias entre `start` e `end`.
2. Use `int()` para converter o resultado em um inteiro e `range()` para iterar sobre cada dia.
3. Use uma compreensão de lista (list comprehension) e `datetime.timedelta` para criar uma lista de objetos `datetime.date`.

```python
from datetime import timedelta, date

def daterange(start, end):
  return [start + timedelta(n) for n in range(int((end - start).days))]
```

```python
from datetime import date

daterange(date(2020, 10, 1), date(2020, 10, 5))
# [date(2020, 10, 1), date(2020, 10, 2), date(2020, 10, 3), date(2020, 10, 4)]
```
