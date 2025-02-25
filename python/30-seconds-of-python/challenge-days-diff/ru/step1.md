# Разница между датами в днях

## Задача

Напишите функцию `days_diff(start, end)`, которая принимает два объекта даты в качестве входных данных и возвращает количество дней между ними. Функция должна вычесть `start` из `end` и использовать `datetime.timedelta.days`, чтобы получить разницу в днях.

## Пример

```python
from datetime import date

assert days_diff(date(2020, 10, 25), date(2020, 10, 28)) == 3
assert days_diff(date(2021, 1, 1), date(2021, 1, 1)) == 0
assert days_diff(date(2021, 1, 1), date(2021, 1, 2)) == 1
```
