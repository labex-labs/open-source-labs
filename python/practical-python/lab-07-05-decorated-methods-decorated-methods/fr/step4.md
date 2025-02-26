# Exercice 7.11 : Utilisation des méthodes de classe

Dans vos fichiers `report.py` et `portfolio.py`, la création d'un objet `Portfolio` est un peu embrouillée. Par exemple, le programme `report.py` a du code comme ceci :

```python
def read_portfolio(filename, **opts):
    '''
    Lit un fichier de portefeuille d'actions dans une liste de dictionnaires avec les clés
    name, shares et price.
    '''
    with open(filename) as lines:
        portdicts = fileparse.parse_csv(lines,
                                        select=['name','shares','price'],
                                        types=[str,int,float],
                                        **opts)

    portfolio = [ Stock(**d) for d in portdicts ]
    return Portfolio(portfolio)
```

et le fichier `portfolio.py` définit `Portfolio()` avec un initialisateur étrange comme ceci :

```python
class Portfolio:
    def __init__(self, holdings):
        self._holdings = holdings
  ...
```

Franchement, la chaîne de responsabilité est un peu confuse car le code est dispersé. Si une classe `Portfolio` est supposée contenir une liste d'instances `Stock`, peut-être devriez-vous modifier la classe pour qu'elle soit un peu plus claire. Comme ceci :

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

Si vous voulez lire un portefeuille à partir d'un fichier CSV, peut-être devriez-vous en faire une méthode de classe :

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

Pour utiliser cette nouvelle classe `Portfolio`, vous pouvez maintenant écrire du code comme ceci :

```python
>>> from portfolio import Portfolio
>>> with open('portfolio.csv') as lines:
...     port = Portfolio.from_csv(lines)
...
>>>
```

Apportez ces modifications à la classe `Portfolio` et modifiez le code de `report.py` pour utiliser la méthode de classe.
