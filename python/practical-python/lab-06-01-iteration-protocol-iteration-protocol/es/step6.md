# Ejercicio 6.3: Creando un contenedor más adecuado

Si estás creando una clase de contenedor, a menudo quieres hacer más que simplemente iterar. Modifica la clase `Portfolio` de modo que tenga algunos otros métodos especiales como este:

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

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

Ahora, intenta algunos experimentos con esta nueva clase:

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> len(portfolio)
7
>>> portfolio[0]
Stock('AA', 100, 32.2)
>>> portfolio[1]
Stock('IBM', 50, 91.1)
>>> portfolio[0:3]
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44)]
>>> 'IBM' in portfolio
True
>>> 'AAPL' in portfolio
False
>>>
```

Una observación importante al respecto: generalmente, el código se considera "pythonista" si habla el vocabulario común de cómo funcionan normalmente otras partes de Python. Para los objetos de contenedor, el soporte para la iteración, la indexación, la contención y otros tipos de operadores es una parte importante de esto.
