# Задаем даты и генерируем случайные данные

Необходимо задать начальную и конечную даты и дельту, которая представляет разницу между каждой датой. Также необходимо сгенерировать случайные данные для примера.

```python
date1 = datetime.date(1952, 1, 1)
date2 = datetime.date(2004, 4, 12)
delta = datetime.timedelta(days=100)

dates = drange(date1, date2, delta)
s = np.random.rand(len(dates))
```
