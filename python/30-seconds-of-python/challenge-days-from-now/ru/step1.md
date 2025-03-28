# Дни от текущей даты

## Задача

Напишите функцию `days_from_now(n)`, которая принимает целое число `n` в качестве входных данных и возвращает дату, которая будет через `n` дней от сегодняшней.

Для решения этой задачи вы можете следовать следующим шагам:

1. Импортируйте модуль `datetime`.
2. Используйте метод `date.today()`, чтобы получить текущую дату.
3. Используйте метод `timedelta`, чтобы добавить `n` дней к текущей дате.
4. Верните новую дату.

## Пример

```python
>>> days_from_now(5)
datetime.date(2022, 12, 28)
>>> days_from_now(10)
datetime.date(2022, 1, 2)
```
