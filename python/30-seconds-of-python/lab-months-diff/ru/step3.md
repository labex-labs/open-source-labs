# Тестирование с различными сценариями дат

Для лучшего понимания того, как наша функция `months_diff` работает с разными сценариями дат, давайте создадим отдельный тестовый файл. Такой подход распространен в разработке программного обеспечения для проверки того, что наш код работает как ожидается.

Создайте новый файл с именем `month_diff_test.py` в директории `/home/labex/project`:

```python
from datetime import date
from month_difference import months_diff

# Test scenario 1: Dates in the same month
date1 = date(2023, 5, 5)
date2 = date(2023, 5, 25)
print(f"Same month: {months_diff(date1, date2)} month(s)")

# Test scenario 2: Consecutive months
date3 = date(2023, 6, 28)
date4 = date(2023, 7, 15)
print(f"Consecutive months: {months_diff(date3, date4)} month(s)")

# Test scenario 3: Dates crossing year boundary
date5 = date(2023, 12, 20)
date6 = date(2024, 1, 10)
print(f"Across years: {months_diff(date5, date6)} month(s)")

# Test scenario 4: Several months apart
date7 = date(2023, 3, 10)
date8 = date(2023, 9, 20)
print(f"Several months: {months_diff(date7, date8)} month(s)")

# Test scenario 5: Dates in reverse order (negative result)
print(f"Reverse order: {months_diff(date8, date7)} month(s)")

# Test scenario 6: Exact multiples of 30 days
date9 = date(2023, 1, 1)
date10 = date(2023, 1, 31)  # 30 days
date11 = date(2023, 3, 2)   # 60 days
print(f"30 days exactly: {months_diff(date9, date10)} month(s)")
print(f"60 days exactly: {months_diff(date9, date11)} month(s)")
```

Сохраните этот файл и запустите его:

```bash
python3 ~/project/month_diff_test.py
```

Вы должны увидеть вывод, похожий на следующий:

```
Same month: 1 month(s)
Consecutive months: 1 month(s)
Across years: 1 month(s)
Several months: 7 month(s)
Reverse order: -7 month(s)
30 days exactly: 1 month(s)
60 days exactly: 2 month(s)
```

Проанализируем эти результаты:

1. **В одном месяце**: Даже внутри одного месяца наша функция возвращает 1 месяц. Это потому, что даже частичный месяц считается полным.

2. **Последовательные месяцы**: Для дат в последовательных месяцах функция возвращает 1 месяц.

3. **Перекрест года**: Для дат, которые пересекают границу года, функция все еще вычисляет корректно.

4. **Разделенные несколькими месяцами**: Для дат, которые разделены несколькими месяцами, функция вычисляет соответствующее количество месяцев.

5. **Обратный порядок**: Когда конечная дата раньше начальной, мы получаем отрицательный результат, что имеет смысл для сценариев, таких как расчет оставшегося времени.

6. **Точные кратные**: Для ровно 30 дней мы получаем 1 месяц. Для 60 дней мы получаем 2 месяца. Это подтверждает, что наша функция работает как ожидается с точными кратными нашей определенной длины месяца.

Наша функция `months_diff` правильно обрабатывает все эти тестовые случаи в соответствии с нашим определением месяца как 30 дней.
