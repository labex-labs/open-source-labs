# Упражнение 7.11: Методы класса на практике

В файлах `report.py` и `portfolio.py` создание объекта `Portfolio` немного запутано. Например, в программе `report.py` есть код такого вида:

```python
def read_portfolio(filename, **opts):
    '''
    Считывает файл портфеля акций в список словарей с ключами
    name, shares и price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

    portfolio = [ Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)
```

а в файле `portfolio.py` `Portfolio()` определяется с странным инициализатором такого вида:

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings
  ...
```

Честно говоря, цепочка ответственности несколько запутана, потому что код рассеян. Если класс `Portfolio` должен содержать список экземпляров `Stock`, возможно, стоит изменить класс, чтобы он был более понятным. Так:

```python
# portfolio.py

import stock

class Portfolio:
    def __init__(self):
        self._holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)
  ...
```

Если вы хотите прочитать портфель из CSV-файла, возможно, стоит сделать для этого метод класса:

```python
# portfolio.py

import fileparse
import stock

class Portfolio:
    def __init__(self):
        self._holdings = []

    def append(self, holding):
        if not isinstance(holding, stock.Stock):
            raise TypeError('Expected a Stock instance')
        self._holdings.append(holding)

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

        for d in portdicts:
            self.append(stock.Stock(**d))

        return self
```

Для использования этого нового класса `Portfolio` теперь можно написать код такого вида:

```python
>>> from portfolio import Portfolio
>>> with open('portfolio.csv') as lines:
...     port = Portfolio.from_csv(lines)
...
>>>
```

Примените эти изменения к классу `Portfolio` и измените код `report.py`, чтобы использовать метод класса.
