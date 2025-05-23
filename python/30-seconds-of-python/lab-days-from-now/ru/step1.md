# Дни от текущей даты

Напишите функцию `days_from_now(n)`, которая принимает целое число `n` в качестве входных данных и возвращает дату, которая будет через `n` дней от сегодняшней.

Для решения этой проблемы вы можете следовать следующим шагам:

1. Импортируйте модуль `datetime`.
2. Используйте метод `date.today()`, чтобы получить текущую дату.
3. Используйте метод `timedelta`, чтобы добавить `n` дней к текущей дате.
4. Верните новую дату.

```python
from datetime import timedelta, date

def days_from_now(n):
  return date.today() + timedelta(n)
```

```python
days_from_now(5) # date(2020, 11, 02)
```
