# Упражнение 2.2: Словарь как структура данных

Вместо кортежа можно создать словарь.

```python
>>> d = {
        'name' : row[0],
      'shares' : int(row[1]),
        'price'  : float(row[2])
    }
>>> d
{'name': 'AA','shares': 100, 'price': 32.2 }
>>>
```

Вычислите общую стоимость этой активации:

```python
>>> cost = d['shares'] * d['price']
>>> cost
3220.0000000000005
>>>
```

Сравните этот пример с тем же вычислением, которое использовалось для кортежей выше. Измените количество акций на 75.

```python
>>> d['shares'] = 75
>>> d
{'name': 'AA','shares': 75, 'price': 32.2 }
>>>
```

В отличие от кортежей, словари можно свободно изменять. Добавьте некоторые атрибуты:

```python
>>> d['date'] = (6, 11, 2007)
>>> d['account'] = 12345
>>> d
{'name': 'AA','shares': 75, 'price':32.2, 'date': (6, 11, 2007), 'account': 12345}
>>>
```
