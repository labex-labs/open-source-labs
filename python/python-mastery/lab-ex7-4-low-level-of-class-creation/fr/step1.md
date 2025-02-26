# Création d'une classe

Rappelez-vous, dans les exercices précédents, nous avons défini une classe simple `Stock` qui ressemblait à ceci :

```python
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares*self.price
    def sell(self,nshares):
        self.shares -= nshares
```

Ce que nous allons faire ici est de créer la classe manuellement. Commencez par définir les méthodes comme de normales fonctions Python.

```python
>>> def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

>>> def cost(self):
        return self.shares*self.price

>>> def sell(self,nshares):
        self.shares -= nshares

>>>
```

Ensuite, créez un dictionnaire de méthodes :

```python
>>> methods = {
         '__init__' : __init__,
         'cost' : cost,
         'sell' : sell }

>>>
```

Enfin, créez l'objet de classe `Stock` :

```python
>>> Stock = type('Stock',(object,),methods)
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>> s.sell(25)
>>> s.shares
75
>>>
```

Félicitations, vous venez de créer une classe. Une classe n'est en réalité rien de plus qu'un nom, un tuple de classes de base et un dictionnaire contenant tous les éléments de la classe. `type()` est un constructeur qui crée une classe pour vous si vous fournissez ces trois parties.
