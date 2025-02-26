# Ejercicio 6.2: Soporte para iteración

En ocasiones, es posible que desees hacer que uno de tus propios objetos soporte la iteración, especialmente si tu objeto envuelve una lista existente u otro iterable. En un nuevo archivo `portfolio.py`, define la siguiente clase:

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

Esta clase está destinada a ser una capa alrededor de una lista, pero con algunos métodos adicionales como la propiedad `total_cost`. Modifica la función `read_portfolio()` en `report.py` de modo que cree una instancia de `Portfolio` de la siguiente manera:

    # report.py

...

    import fileparse
    from stock import Stock
    from portfolio import Portfolio

    def read_portfolio(filename):
        '''
        Lee un archivo de cartera de acciones en una lista de diccionarios con claves
        name, shares y price.
        '''
        with open(filename) as file:
            portdicts = fileparse.parse_csv(file,
                                            select=['name','shares','price'],
                                            types=[str,int,float])

        portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
        return Portfolio(portfolio)

...

Intenta ejecutar el programa `report.py`. Verás que fallará espectacularmente debido a que las instancias de `Portfolio` no son iterables.

```python
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... se detiene...
```

Corrige esto modificando la clase `Portfolio` para que soporte la iteración:

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

Después de hacer este cambio, tu programa `report.py` debería funcionar de nuevo. Mientras estás en ello, corrige tu programa `pcost.py` para que utilice el nuevo objeto `Portfolio`. De la siguiente manera:

```python
# pcost.py

import report

def portfolio_cost(filename):
    '''
    Calcula el costo total (shares*price) de un archivo de cartera de acciones
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
...
```

Prueba para asegurarte de que funcione:

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>>
```
