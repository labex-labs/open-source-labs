# Dicts et Objets

Les objets définis par l'utilisateur utilisent également des dictionnaires pour les données d'instance et les classes. En fait, tout le système d'objets est principalement une couche supplémentaire qui est placée au-dessus des dictionnaires.

Un dictionnaire contient les données d'instance, `__dict__`.

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{'name' : 'GOOG','shares' : 100, 'price': 490.1 }
```

Vous remplit ce dictionnaire (et l'instance) en affectant à `self`.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Les données d'instance, `self.__dict__`, ressemblent à ceci :

```python
{
    'name': 'GOOG',
   'shares': 100,
    'price': 490.1
}
```

**Chaque instance obtient son propre dictionnaire privé.**

```python
s = Stock('GOOG', 100, 490.1)     # {'name' : 'GOOG','shares' : 100, 'price': 490.1 }
t = Stock('AAPL', 50, 123.45)     # {'name' : 'AAPL','shares' : 50, 'price': 123.45 }
```

Si vous avez créé 100 instances d'une certaine classe, il y a 100 dictionnaires qui contiennent des données.
