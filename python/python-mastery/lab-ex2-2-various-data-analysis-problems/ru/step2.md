# Comprehensions

List, set, и dictionary comprehensions могут быть полезным инструментом для манипуляции данными. Например, попробуйте эти операции:

```python
>>> # Найти все позиции, где количество акций больше 100
>>> [s for s in portfolio if s['shares'] > 100]
[{'name': 'CAT','shares': 150, 'price': 83.44},
 {'name': 'MSFT','shares': 200, 'price': 51.23}]

>>> # Вычислить общую стоимость (количество акций * цена)
>>> sum([s['shares']*s['price'] for s in portfolio])
44671.15
>>>

>>> # Найти все уникальные названия акций (множество)
>>> { s['name'] for s in portfolio }
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
>>>

>>> # Подсчитать общее количество акций каждой компании
>>> totals = { s['name']: 0 for s in portfolio }
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
>>>
```
