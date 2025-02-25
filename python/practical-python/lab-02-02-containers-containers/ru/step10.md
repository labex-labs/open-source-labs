# Упражнение 2.5: Список словарей

Возьмите функцию, которую вы написали в упражнении 2.4, и модифицируйте ее так, чтобы каждый акция в портфеле представлялась словарем, а не кортежем. В этом словаре используйте имена полей "name", "shares" и "price", чтобы представить разные колонки в входном файле.

Протестируйте эту новую функцию так же, как вы делали это в упражнении 2.4.

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1},
    {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23},
    {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1},
    {'name': 'IBM','shares': 100, 'price': 70.44}]
>>> portfolio[0]
{'name': 'AA','shares': 100, 'price': 32.2}
>>> portfolio[1]
{'name': 'IBM','shares': 50, 'price': 91.1}
>>> portfolio[1]['shares']
50
>>> total = 0.0
>>> for s in portfolio:
        total += s['shares']*s['price']

>>> print(total)
44671.15
>>>
```

Здесь вы заметите, что разные поля для каждой записи доступа по именам ключей, а не по числовым номерам колонок. Это часто предпочтительнее, потому что результирующий код легче читать позднее.

Просмотр больших словарей и списков может быть запутанным. Чтобы очистить вывод для отладки, рассмотрите использование функции `pprint`.

```python
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2,'shares': 100},
    {'name': 'IBM', 'price': 91.1,'shares': 50},
    {'name': 'CAT', 'price': 83.44,'shares': 150},
    {'name': 'MSFT', 'price': 51.23,'shares': 200},
    {'name': 'GE', 'price': 40.37,'shares': 95},
    {'name': 'MSFT', 'price': 65.1,'shares': 50},
    {'name': 'IBM', 'price': 70.44,'shares': 100}]
>>>
```
