# Определяем даты и дельту

Далее мы будем определять даты и значения дельты с использованием библиотеки datetime. Диапазон дат будет от 2 марта 2000 года до 6 марта 2000 года с интервалом в 6 часов. Скопируйте и вставьте следующий код:

```python
date1 = datetime.datetime(2000, 3, 2)
date2 = datetime.datetime(2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)
```
