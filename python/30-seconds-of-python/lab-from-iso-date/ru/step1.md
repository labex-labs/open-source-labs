# Преобразование даты в формате ISO

Напишите функцию `from_iso_date(d)`, которая принимает строку `d`, представляющую дату в формате ISO-8601, и возвращает объект `datetime.datetime`, представляющий ту же дату и время.

```python
from datetime import datetime

def from_iso_date(d):
  return datetime.fromisoformat(d)
```

```python
from_iso_date('2020-10-28T12:30:59.000000') # 2020-10-28 12:30:59
```
