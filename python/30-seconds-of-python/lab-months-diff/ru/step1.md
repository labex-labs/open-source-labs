# Разница между датами

Напишите функцию с именем `months_diff(start, end)`, которая принимает два объекта даты и возвращает разницу в месяцах между ними. Функция должна:

1. Вычесть `start` из `end` и использовать `datetime.timedelta.days`, чтобы получить разницу в днях.
2. Разделить на `30` и использовать `math.ceil()`, чтобы получить разницу в месяцах (округленную вверх).

```python
from math import ceil

def months_diff(start, end):
  return ceil((end - start).days / 30)
```

```python
from datetime import date

months_diff(date(2020, 10, 28), date(2020, 11, 25)) # 1
```
