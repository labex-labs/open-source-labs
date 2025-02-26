# Ejercicio 7.11: Métodos de clase en la práctica

En sus archivos `report.py` y `portfolio.py`, la creación de un objeto `Portfolio` está un poco confusa. Por ejemplo, el programa `report.py` tiene código como este:

```python
def read_portfolio(filename, **opts):
    '''
    Lee un archivo de cartera de acciones en una lista de diccionarios con claves
    name, shares y price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

    portfolio = [ Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)
```

y el archivo `portfolio.py` define `Portfolio()` con un inicializador extraño como este:

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings
  ...
```

Frankmente, la cadena de responsabilidad es un poco confusa porque el código está disperso. Si una clase `Portfolio` está supuesta a contener una lista de instancias de `Stock`, quizás debería cambiar la clase para que sea un poco más clara. Así:

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

Si desea leer una cartera desde un archivo CSV, quizás debería crear un método de clase para ello:

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

Para usar esta nueva clase `Portfolio`, ahora puede escribir código como este:

```python
>>> from portfolio import Portfolio
>>> with open('portfolio.csv') as lines:
...     port = Portfolio.from_csv(lines)
...
>>>
```

Haga estos cambios a la clase `Portfolio` y modifique el código de `report.py` para usar el método de clase.
