# Exercice 6.2 : Prise en charge de l'itération

Parfois, vous souhaiterez peut-être que l'un de vos propres objets prenne en charge l'itération - en particulier si votre objet encapsule une liste existante ou un autre itérable. Dans un nouveau fichier `portfolio.py`, définissez la classe suivante :

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

Cette classe est censée être une couche autour d'une liste, mais avec quelques méthodes supplémentaires telles que la propriété `total_cost`. Modifiez la fonction `read_portfolio()` dans `report.py` de manière à ce qu'elle crée une instance de `Portfolio` comme ceci :

    # report.py

...

    import fileparse
    from stock import Stock
    from portfolio import Portfolio

    def read_portfolio(filename):
        '''
        Lit un fichier de portefeuille d'actions dans une liste de dictionnaires avec les clés
        name, shares et price.
        '''
        with open(filename) as file:
            portdicts = fileparse.parse_csv(file,
                                            select=['name','shares','price'],
                                            types=[str,int,float])

        portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
        return Portfolio(portfolio)

...

Essayez d'exécuter le programme `report.py`. Vous constaterez qu'il échoue de manière spectaculaire en raison du fait que les instances de `Portfolio` ne sont pas itérables.

```python
>>> import report
>>> report.portfolio_report('portfolio.csv', 'prices.csv')
... plante...
```

Corrigez ce problème en modifiant la classe `Portfolio` pour qu'elle prenne en charge l'itération :

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

Après avoir effectué ce changement, votre programme `report.py` devrait fonctionner à nouveau. Pendant que vous y êtes, corrigez votre programme `pcost.py` pour utiliser le nouveau `Portfolio` objet. Comme ceci :

```python
# pcost.py

import report

def portfolio_cost(filename):
    '''
    Calcule le coût total (shares*price) d'un fichier de portefeuille
    '''
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost
...
```

Testez-le pour vous assurer qu'il fonctionne :

```python
>>> import pcost
>>> pcost.portfolio_cost('portfolio.csv')
44671.15
>>>
```
