# Дни назад

Ваша задача - написать функцию под названием `days_ago(n)`, которая принимает целое число `n` в качестве аргумента и возвращает дату, которая была `n` дней назад от сегодняшней.

Для решения этой проблемы вам нужно использовать класс `date` из модуля `datetime`, чтобы получить текущую дату, и класс `timedelta`, чтобы вычесть `n` дней из текущей даты.

```python
from datetime import timedelta, date

def days_ago(n):
  return date.today() - timedelta(n)
```

```python
days_ago(5) # date(2020, 10, 23)
```
