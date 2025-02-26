# Вызов к действию

Что произойдет, если вы сделаете срез данных о поездках?

```python
>>> r = rows[0:10]
>>> r
... look at result...
>>>
```

Вероятно, это будет выглядеть немного странно. Можете ли вы изменить класс `RideData`, чтобы он возвращал правильный срез, который будет выглядеть как список словарей? Например, так:

```python
>>> rows = readrides.read_rides_as_columns('ctabus.csv')
>>> rows
<readrides.RideData object at 0x10f5054a8>
>>> len(rows)
577563
>>> r = rows[0:10]
>>> r
<readrides.RideData object at 0x10f5068c8>
>>> len(r)
10
>>> r[0]
{'route': '3', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
>>> r[1]
{'route': '4', 'date': '01/01/2001', 'daytype': 'U', 'rides': 9288}
>>>
```
