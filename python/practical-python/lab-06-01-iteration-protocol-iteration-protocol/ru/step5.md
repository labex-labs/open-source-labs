# Упражнение 6.2: Поддержка итерации

Иногда вы можете захотеть, чтобы один из своих собственных объектов поддерживал итерацию - особенно если ваш объект оборачивает существующий список или другой итерируемый объект. В новом файле `portfolio.py` определите следующий класс:

```python
# portfolio.py

class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

Этот класс предназначен для обертки вокруг списка, но с некоторыми дополнительными методами, такими как свойство `total_cost`. Измените функцию `read_portfolio()` в `report.py`, чтобы она создавала экземпляр `Portfolio` так:

    # report.py

...

    import fileparse
    from stock import Stock
    from portfolio import Portfolio

    def read_portfolio(filename):
        '''
        Считывает файл портфеля акций в список словарей с ключами
        name, shares и price.
        '''
        with open(filename) as file:
            portdicts = fileparse.parse_csv(file,
                                            select=['name','shares','price'],
                                            types=[str,int,float])

        portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
        return Portfolio(portfolio)

...

Попробуйте запустить программу `report.py`. Вы обнаружите, что она spectacularly завершается из-за того, что экземпляры `Portfolio` не итерируемы.

```python
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... crashes...
```

Исправьте это, изменив класс `Portfolio` для поддержки итерации:

```python
class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    @property
    def total_cost(self):
        return sum([s.shares*s.price for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
```

После внесения этих изменений программа `report.py` должна снова работать. В то же время исправьте программу `pcost.py`, чтобы она использовала новый объект `Portfolio`. Так:

```python
# pcost.py

import report

def portfolio_cost(filename):
    '''
    Вычисляет общую стоимость (количество акций * цена) файла портфеля
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
...
```

Протестируйте ее, чтобы убедиться, что все работает:

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>>
```
