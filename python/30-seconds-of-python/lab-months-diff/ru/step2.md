# Создание функции для вычисления разницы в месяцах

Теперь, когда мы понимаем, как работать с объектами даты и вычислять разницу в днях, давайте создадим функцию для вычисления разницы в месяцах.

В многих приложениях месяц приблизительно оценивается как 30 дней. Хотя это не всегда точно (месяцы могут иметь от 28 до 31 день), это распространенное упрощение, которое хорошо работает для многих бизнес - расчетов.

Откройте файл `month_difference.py` и добавьте следующую функцию ниже существующего кода:

```python
def months_diff(start, end):
    """
    Calculate the difference in months between two dates.

    Args:
        start (date): The start date
        end (date): The end date

    Returns:
        int: The number of months between the dates (rounded up)
    """
    # Calculate the difference in days
    days_difference = (end - start).days

    # Convert days to months (assuming 30 days per month) and round up
    months = ceil(days_difference / 30)

    return months
```

Понять, что делает эта функция:

1. Она принимает два параметра: `start` и `end`, которые являются объектами даты.
2. Она вычисляет разницу в днях между этими датами.
3. Она делит на 30, чтобы преобразовать дни в месяцы.
4. Она использует функцию `ceil()`, чтобы округлить вверх до ближайшего целого числа.
5. Она возвращает результат в виде целого числа.

Функция `ceil()` используется, потому что во многих бизнес - сценариях даже частичный месяц учитывается как полный месяц для выставления счетов.

Чтобы протестировать нашу функцию, добавьте следующий код в конце файла:

```python
# Test the months_diff function with our example dates
print(f"Months between {date1} and {date2}: {months_diff(date1, date2)}")

# Test with some other date pairs
print(f"Months between 2020-10-28 and 2020-11-25: {months_diff(date(2020, 10, 28), date(2020, 11, 25))}")
print(f"Months between 2020-12-15 and 2021-01-10: {months_diff(date(2020, 12, 15), date(2021, 01, 10))}")
```

Сохраните файл и запустите его снова:

```bash
python3 ~/project/month_difference.py
```

Вы должны увидеть вывод, похожий на следующий:

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
Months between 2023-01-15 and 2023-03-20: 3
Months between 2020-10-28 and 2020-11-25: 1
Months between 2020-12-15 and 2021-01-10: 1
```

Обратите внимание, что:

- 64 дня между 2023 - 01 - 15 и 2023 - 03 - 20 вычисляются как 3 месяца (64/30 = 2.13, округлено вверх до 3).
- Разница между 28 октября и 25 ноября вычисляется как 1 месяц.
- Разница между 15 декабря и 10 января (через границу года) также вычисляется как 1 месяц.
