# Диапазон дат

Напишите функцию на Python под названием `daterange(start, end)`, которая принимает два объекта `datetime.date` в качестве аргументов и возвращает список всех дат между ними. Список должен включать начальную дату, но не конечную.

Для решения этой проблемы вы можете следовать следующим шагам:

1. Используйте `datetime.timedelta.days`, чтобы получить количество дней между `start` и `end`.
2. Используйте `int()`, чтобы преобразовать результат в целое число, и `range()`, чтобы перебрать каждый день.
3. Используйте списочное выражение и `datetime.timedelta`, чтобы создать список объектов `datetime.date`.

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
