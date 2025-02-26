# Упражнение 2.21: Запросы к данным

Попробуйте следующие примеры различных запросов к данным.

Во - первых, список всех позиций портфеля с количеством акций более 100.

```python
>>> more100 = [ s for s in portfolio if s['shares'] > 100 ]
>>> more100
[{'price': 83.44, 'name': 'CAT','shares': 150}, {'price': 51.23, 'name': 'MSFT','shares': 200}]
>>>
```

Все позиции портфеля для акций MSFT и IBM.

```python
>>> msftibm = [ s for s in portfolio if s['name'] in {'MSFT','IBM'} ]
>>> msftibm
[{'price': 91.1, 'name': 'IBM','shares': 50}, {'price': 51.23, 'name': 'MSFT','shares': 200},
  {'price': 65.1, 'name': 'MSFT','shares': 50}, {'price': 70.44, 'name': 'IBM','shares': 100}]
>>>
```

Список всех позиций портфеля, стоимость которых превышает 10000 долларов.

```python
>>> cost10k = [ s for s in portfolio if s['shares'] * s['price'] > 10000 ]
>>> cost10k
[{'price': 83.44, 'name': 'CAT','shares': 150}, {'price': 51.23, 'name': 'MSFT','shares': 200}]
>>>
```
