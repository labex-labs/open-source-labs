# Structures de données simplifiées

Dans les exercices précédents, vous avez défini une classe représentant une action comme ceci :

```python
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Prenez en compte la méthode `__init__()` - n'est-ce pas beaucoup de code à taper chaque fois que vous voulez initialiser une structure? Et si vous deviez définir des dizaines de telles structures dans votre programme?

Dans un fichier `structure.py`, définissez une classe de base `Structure` qui permet à l'utilisateur de définir des structures de données simples comme suit :

```python
class Stock(Structure):
    _fields = ('name','shares','price')

class Date(Structure):
    _fields = ('year','month', 'day')
```

La classe `Structure` devrait définir une méthode `__init__()` qui prend un nombre quelconque d'arguments et qui cherche la présence d'une variable de classe `_fields`. Faites en sorte que la méthode initialise l'instance à partir des noms d'attributs dans `_fields` et des valeurs passées à `__init__()`.

Voici un exemple de code pour tester votre implémentation :

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s = Stock('AA',50)
Traceback (most recent call last):
...
TypeError: Expected 3 arguments
>>>
```
