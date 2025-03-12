# Manual Class Creation

In traditional Python programming, we define classes using the standard syntax. For example, a simple `Stock` class might look like this:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

What if we wanted to create this class without using the standard class syntax? Let's explore how Python classes are constructed at a lower level.

## Launch Python Interactive Shell

Open a terminal in WebIDE and start the Python interactive shell by typing:

```bash
cd ~/project
python3
```

## Defining Methods as Regular Functions

First, let's define the methods we want in our class as regular Python functions:

```python
def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

def sell(self, nshares):
    self.shares -= nshares
```

## Creating a Methods Dictionary

Next, we need to create a dictionary that will contain all the methods for our class:

```python
methods = {
    '__init__': __init__,
    'cost': cost,
    'sell': sell
}
```

## Using type() Constructor to Create a Class

Now, we can use the `type()` constructor to create our class. The `type()` function takes three arguments:

1. The name of the class
2. A tuple of base classes
3. A dictionary containing methods and attributes

```python
Stock = type('Stock', (object,), methods)
```

## Testing Our Manually Created Class

Let's create an instance of our new class and test its methods:

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
s.sell(25)
print(s.shares)
```

You should see the following output:

```
GOOG
49010.0
75
```

This demonstrates that a class is fundamentally just a name, a tuple of base classes, and a dictionary of methods and attributes. The `type()` function simply constructs a class object from these components.

Exit the Python shell when you're done:

```python
exit()
```
