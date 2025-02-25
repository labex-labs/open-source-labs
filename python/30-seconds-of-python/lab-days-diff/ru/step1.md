# Разница между датами в днях

Напишите функцию `days_diff(start, end)`, которая принимает два объекта даты в качестве входных данных и возвращает количество дней между ними. Функция должна вычесть `start` из `end` и использовать `datetime.timedelta.days`, чтобы получить разницу в днях.

```python
def days_diff(start, end):
  return (end - start).days
```

```python
from datetime import date

days_diff(date(2020, 10, 25), date(2020, 10, 28)) # 3
```
