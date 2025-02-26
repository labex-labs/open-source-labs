# Variables de classe et héritage

Les variables de classe telles que `types` sont parfois utilisées comme un mécanisme de personnalisation lorsqu'on utilise l'héritage. Par exemple, dans la classe `Stock`, les types peuvent être facilement modifiés dans une sous-classe. Essayez cet exemple qui change l'attribut `price` en une instance de `Decimal` (qui est souvent mieux adaptée aux calculs financiers) :

```python
>>> from decimal import Decimal
>>> class DStock(Stock):
        types = (str, int, Decimal)

>>> row = ['AA', '100', '32.20']
>>> s = DStock.from_row(row)
>>> s.price
Decimal('32.20')
>>> s.cost()
Decimal('3220.0')
>>>
```

**Discussion sur la conception**

Le problème abordé dans ce laboratoire concerne la conversion des données lues à partir d'un fichier. Est-ce que cela aurait du sens de réaliser ces conversions dans la méthode `__init__()` de la classe `Stock` au lieu de cela? Par exemple :

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

En faisant cela, vous convertiriez une ligne de données comme suit :

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock(*row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>>
```

Est-ce bon ou mauvais? Qu'en pensez-vous? Dans l'ensemble, je pense que c'est une conception douteuse car elle mélange deux choses différentes - la création d'une instance et la conversion des données. De plus, les conversions implicites dans `__init__()` limitent la flexibilité et pourraient introduire des bugs étranges si un utilisateur n'y prête pas attention.
