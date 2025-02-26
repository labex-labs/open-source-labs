# Attributs simples

Considérez la classe suivante.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Une caractéristique surprenante est que vous pouvez attribuer à ces attributs n'importe quelle valeur :

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares = 100
>>> s.shares = "hundred"
>>> s.shares = [1, 0, 0]
>>>
```

Vous pourriez regarder cela et penser que vous voulez des vérifications supplémentaires.

```python
s.shares = '50'     # Levée d'une TypeError, il s'agit d'une chaîne de caractères
```

Comment le feriez-vous?
