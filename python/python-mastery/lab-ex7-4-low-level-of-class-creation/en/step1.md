# Manual Class Creation

In Python programming, classes are a fundamental concept that allows you to group data and functions together. Usually, we define classes using the standard Python syntax. For example, here's a simple `Stock` class. This class represents a stock with attributes like `name`, `shares`, and `price`, and it has methods to calculate the cost and sell shares.

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

But have you ever wondered how Python actually creates a class behind the scenes? What if we wanted to create this class without using the standard class syntax? In this section, we'll explore how Python classes are constructed at a lower level.

## Launch Python Interactive Shell

To start experimenting with manual class creation, we need to open a Python interactive shell. This shell allows us to execute Python code line by line, which is great for learning and testing.

Open a terminal in WebIDE and start the Python interactive shell by typing the following commands. The first command `cd ~/project` changes the current directory to the project directory, and the second command `python3` starts the Python 3 interactive shell.

```bash
cd ~/project
python3
```

## Defining Methods as Regular Functions

Before we create a class manually, we need to define the methods that will be part of the class. In Python, methods are just functions that are associated with a class. So, let's define the methods we want in our class as regular Python functions.

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

Here, the `__init__` function is a special method in Python classes. It's called a constructor, and it's used to initialize the object's attributes when an instance of the class is created. The `cost` method calculates the total cost of the shares, and the `sell` method reduces the number of shares.

## Creating a Methods Dictionary

Now that we have defined our methods as regular functions, we need to organize them in a way that Python can understand when creating the class. We do this by creating a dictionary that will contain all the methods for our class.

```python
methods = {
    '__init__': __init__,
    'cost': cost,
    'sell': sell
}
```

In this dictionary, the keys are the names of the methods as they will be used in the class, and the values are the actual function objects we defined earlier.

## Using type() Constructor to Create a Class

In Python, the `type()` function is a built - in function that can be used to create classes at a lower level. The `type()` function takes three arguments:

1. The name of the class: This is a string that represents the name of the class we want to create.
2. A tuple of base classes: In Python, classes can inherit from other classes. Here, we use `(object,)` which means our class inherits from the base `object` class, which is the base class for all classes in Python.
3. A dictionary containing methods and attributes: This is the dictionary we created earlier that holds all the methods of our class.

```python
Stock = type('Stock', (object,), methods)
```

This line of code creates a new class named `Stock` using the `type()` function. The class inherits from the `object` class and has the methods defined in the `methods` dictionary.

## Testing Our Manually Created Class

Now that we have created our class manually, let's test it to make sure it works as expected. We'll create an instance of our new class and call its methods.

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
s.sell(25)
print(s.shares)
```

In the first line, we create an instance of the `Stock` class with the name `GOOG`, 100 shares, and a price of 490.10. Then we print the name of the stock, calculate and print the cost, sell 25 shares, and finally print the remaining number of shares.

You should see the following output:

```
GOOG
49010.0
75
```

This output shows that our manually created class works just like a class created using the standard Python syntax. It demonstrates that a class is fundamentally just a name, a tuple of base classes, and a dictionary of methods and attributes. The `type()` function simply constructs a class object from these components.

Exit the Python shell when you're done:

```python
exit()
```
