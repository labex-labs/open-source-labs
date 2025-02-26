# Klassenerstellung

Denken Sie sich aus früheren Übungen zurück, wir haben eine einfache Klasse `Stock` definiert, die so aussah:

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

Was wir hier tun werden, ist die Klasse manuell zu erstellen. Beginnen Sie damit, die Methoden einfach als normale Python-Funktionen zu definieren.

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

Als nächstes erstellen Sie ein Methoden-Dictionary:

```python
>>> methods = {
         '__init__' : __init__,
         'cost' : cost,
         'sell' : sell }

>>>
```

Schließlich erstellen Sie das `Stock`-Klassenobjekt:

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

Herzlichen Glückwunsch, Sie haben gerade eine Klasse erstellt. Eine Klasse ist eigentlich nichts weiter als ein Name, ein Tupel von Basisklassen und ein Dictionary, das alle Inhalte der Klasse enthält. `type()` ist ein Konstruktor, der Ihnen eine Klasse erstellt, wenn Sie diese drei Teile angeben.
