# Exercício 7.11: Métodos de Classe na Prática

Nos seus arquivos `report.py` e `portfolio.py`, a criação de um objeto `Portfolio` é um pouco confusa. Por exemplo, o programa `report.py` tem um código como este:

```python
def read_portfolio(filename, **opts):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

    portfolio = [ Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)
```

e o arquivo `portfolio.py` define `Portfolio()` com um inicializador estranho como este:

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings
    ...
```

Francamente, a cadeia de responsabilidade é um pouco confusa porque o código está disperso. Se uma classe `Portfolio` deve conter uma lista de instâncias `Stock`, talvez você devesse mudar a classe para ser um pouco mais clara. Assim:

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

Se você quiser ler um portfólio de um arquivo CSV, talvez devesse criar um método de classe para isso:

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

Para usar esta nova classe Portfolio, você pode agora escrever um código como este:

```python
>>> from portfolio import Portfolio
>>> with open('portfolio.csv') as lines:
...     port = Portfolio.from_csv(lines)
...
>>>
```

Faça estas alterações na classe `Portfolio` e modifique o código `report.py` para usar o método de classe.
