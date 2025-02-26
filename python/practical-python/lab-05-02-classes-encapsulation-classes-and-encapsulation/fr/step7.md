# Propriétés

Il existe une approche alternative au modèle précédent.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

L'accès aux attributs normaux déclenche désormais les méthodes getter et setter situées sous `@property` et `@shares.setter`.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares         # Décenche @property
50
>>> s.shares = 75    # Décenche @shares.setter
>>>
```

Avec ce modèle, il n'est _pas nécessaire_ d'apporter de modifications au code source. Le nouveau _setter_ est également appelé lorsqu'il y a une affectation à l'intérieur de la classe, y compris à l'intérieur de la méthode `__init__()`.

```python
class Stock:
    def __init__(self, name, shares, price):
     ...
        # Cette affectation appelle le setter ci-dessous
        self.shares = shares
     ...

  ...
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
```

Il existe souvent une confusion entre une propriété et l'utilisation de noms privés. Bien qu'une propriété utilise internement un nom privé comme `_shares`, le reste de la classe (et non la propriété) peut continuer à utiliser un nom comme `shares`.

Les propriétés sont également utiles pour les attributs de données calculés.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price
  ...
```

Cela vous permet d'omettre les parenthèses supplémentaires, cachant le fait qu'il s'agit en réalité d'une méthode :

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares # Variable d'instance
100
>>> s.cost   # Valeur calculée
49010.0
>>>
```
