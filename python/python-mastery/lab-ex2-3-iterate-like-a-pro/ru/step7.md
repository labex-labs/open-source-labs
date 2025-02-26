# Экономия памяти

В упражнении 2.1 вы написали функцию `read_rides_as_dicts()`, которая считывает данные автобусов CTA в список словарей. Использование этой функции требует большого количества памяти. Например, давайте найдем день, в который на маршруте 22 автобуса было наибольшее количество пассажиров:

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rt22 = [row for row in rows if row['route'] == '22']
>>> max(rt22, key=lambda row: row['rides'])
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... посмотрите на результат. Должен быть около 220МБ
>>>
```

Теперь давайте попробуем пример, связанный с генераторами. Перезапустите Python и попробуйте это:

```python
>>> # RESTART
>>> import tracemalloc
>>> tracemalloc.start()
>>> import csv
>>> f = open('ctabus.csv')
>>> f_csv = csv.reader(f)
>>> headers = next(f_csv)
>>> rows = (dict(zip(headers,row)) for row in f_csv)
>>> rt22 = (row for row in rows if row['route'] == '22')
>>> max(rt22, key=lambda row: int(row['rides']))
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... посмотрите на результат. Должен быть значительно меньше, чем раньше
>>>
```

Обратите внимание, что вы обработали весь набор данных, будто они были сохранены в виде последовательности словарей. Тем не менее, нигде вы не создавали и не сохраняли список словарей. Не все проблемы могут быть структурированы таким образом, но если вы можете работать с данными итеративным способом, генераторные выражения могут экономить огромное количество памяти.
