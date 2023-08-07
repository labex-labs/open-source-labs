# Create your first metaclass

Create a file called `mymeta.py`
and put the following code in it (from the slides):

```python
# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass
```

Once you've done this, define a class that inherits from
`myobject` instead of object. For example:

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
    def sell(self, nshares):
        self.shares -= nshares
```

Try running your code and creating instances of `Stock`. See
what happens. You should see the print statements from your
`mytype` running once when the `Stock` class is
defined.

What happens if you inherit from `Stock`?

```python
class MyStock(Stock):
    pass
```

You should still see your metaclass at work. Metaclasses are "sticky" in that they
get applied across an entire inheritance hierarchy.

**Discussion**

Why would you want to do something like this?
The main power of a metaclass is that it gives a programmer the ability
to capture details about classes just prior to their creation. For
example, in the `__new__()` method, you are given all of the
basic details including the name of the class, base classes, and
methods data. If you inspect this data, you can perform various
types of diagnostic checks. If you're more daring, you can modify the
data and change what gets placed in the class definition when it is
created. Needless to say, there are many opportunities for horrible
diabolical evil.
