# Class creation

Recall, from earlier exercises, we defined a simple class `Stock` that looked like this:

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

What we're going to do here is create the class manually. Start out by just defining the methods as normal Python functions.

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

Next, make a methods dictionary:

```python
>>> methods = {
         '__init__' : __init__,
         'cost' : cost,
         'sell' : sell }

>>>
```

Finally, create the `Stock` class object:

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

Congratulations, you just created a class. A class is really nothing more than a name, a tuple of base classes, and a dictionary holding all of the class contents. `type()` is a constructor that creates a class for you if you supply these three parts.
