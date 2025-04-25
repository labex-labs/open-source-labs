# 练习 2.5：字典列表

采用你在练习 2.4 中编写的函数，并进行修改，用字典而非元组来表示投资组合中的每只股票。在这个字典中，使用“name”（名称）、“shares”（股数）和“price”（价格）这些字段名来表示输入文件中的不同列。

按照你在练习 2.4 中的方式对这个新函数进行试验。

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

在这里，你会注意到每个条目的不同字段是通过键名而非数字列号来访问的。这通常更受青睐，因为这样生成的代码日后更易于阅读。

查看大型字典和列表可能会很杂乱。为了清理输出以便调试，可以考虑使用 `pprint` 函数。

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
