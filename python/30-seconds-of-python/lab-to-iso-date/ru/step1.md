# Дата в формат ISO

Напишите функцию `to_iso_date(d)`, которая принимает объект `datetime.datetime` в качестве аргумента и возвращает строку, представляющую дату в формате ISO-8601. Функция должна использовать метод `datetime.datetime.isoformat()` для преобразования даты в ее представление в формате ISO-8601.

```python
from datetime import datetime

def to_iso_date(d):
  return d.isoformat()
```

```python
from datetime import datetime

to_iso_date(datetime(2020, 10, 25)) # 2020-10-25T00:00:00
```
