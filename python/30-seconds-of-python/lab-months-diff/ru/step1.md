# Понимание объектов даты в Python

Перед тем как вычислить разницу между датами в месяцах, нам нужно понять, как работать с объектами даты в Python. На этом этапе мы узнаем о модуле `datetime` и создадим несколько объектов даты.

Сначала создадим новый файл Python в директории проекта. Откройте WebIDE и нажмите на иконку "Новый файл" в панели проводника слева. Назовите файл `month_difference.py` и сохраните его в директории `/home/labex/project`.

Теперь добавьте следующий код для импорта необходимых модулей:

```python
from datetime import date
from math import ceil

# Create example date objects
date1 = date(2023, 1, 15)  # January 15, 2023
date2 = date(2023, 3, 20)  # March 20, 2023

# Print the dates to see their format
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")

# Calculate the difference in days
day_difference = (date2 - date1).days
print(f"Difference in days: {day_difference}")
```

Сохраните файл и запустите его с помощью терминала:

```bash
python3 ~/project/month_difference.py
```

Вы должны увидеть вывод, похожий на следующий:

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
```

Класс `date` из модуля `datetime` позволяет нам создавать объекты даты, указав год, месяц и день. Когда мы вычитаем одну дату из другой, Python возвращает объект `timedelta`. Мы можем получить количество дней в этом объекте, используя атрибут `.days`.

В этом примере между 15 января 2023 года и 20 марта 2023 года прошло 64 дня.
