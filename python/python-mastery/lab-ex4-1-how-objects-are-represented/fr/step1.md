# Préparation

Pour commencer ce laboratoire, revenez à une version simple de la classe `Stock` que vous avez créée. Au prompt interactif, définissez une nouvelle classe appelée `SimpleStock` qui ressemble à ceci :

```python
>>> class SimpleStock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        def cost(self):
            return self.shares * self.price

>>>
```

Une fois que vous avez défini cette classe, créez quelques instances.

```python
>>> goog = SimpleStock('GOOG',100,490.10)
>>> ibm  = SimpleStock('IBM',50, 91.23)
>>>
```
