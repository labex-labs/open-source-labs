# Using locals() to Access Function Arguments

In Python, understanding variable scopes is crucial. A variable's scope determines where in the code it can be accessed. Python provides a built - in function called `locals()` that is very handy for beginners to understand scoping. The `locals()` function returns a dictionary containing all local variables in the current scope. This can be extremely useful when you want to inspect function arguments, as it gives you a clear view of what variables are available within a specific part of your code.

Let's create a simple experiment in the Python interpreter to see how this works. First, we need to navigate to the project directory and start the Python interpreter. You can do this by running the following commands in your terminal:

```bash
cd ~/project
python3
```

Once you're in the Python interactive shell, we'll define a `Stock` class. A class in Python is like a blueprint for creating objects. In this class, we'll use the special `__init__` method. The `__init__` method is a constructor in Python, which means it gets called automatically when an object of the class is created. Inside this `__init__` method, we'll use the `locals()` function to print all local variables.

```python
class Stock:
    def __init__(self, name, shares, price):
        print(locals())
```

Now, let's create an instance of this `Stock` class. An instance is an actual object created from the class blueprint. We'll pass in some values for the `name`, `shares`, and `price` parameters.

```python
s = Stock('GOOG', 100, 490.1)
```

When you run this code, you should see output similar to:

```
{'self': <__main__.Stock object at 0x...>, 'name': 'GOOG', 'shares': 100, 'price': 490.1}
```

This output shows that `locals()` gives us a dictionary containing all the local variables in the `__init__` method. The `self` reference is a special variable in Python classes that refers to the instance of the class itself. The other variables are the parameter values we passed when creating the `Stock` object.

We can use this `locals()` functionality to automatically initialize object attributes. Attributes are variables associated with an object. Let's define a helper function and modify our `Stock` class.

```python
def _init(locs):
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)

class Stock:
    def __init__(self, name, shares, price):
        _init(locals())
```

The `_init` function takes the dictionary of local variables obtained from `locals()`. It first removes the `self` reference from the dictionary using the `pop` method. Then, it iterates over the remaining key - value pairs in the dictionary and uses the `setattr` function to set each variable as an attribute on the object.

Now, let's test this implementation with both positional and keyword arguments. Positional arguments are passed in the order they are defined in the function signature, while keyword arguments are passed with the parameter names specified.

```python
# Test with positional arguments
s1 = Stock('GOOG', 100, 490.1)
print(s1.name, s1.shares, s1.price)

# Test with keyword arguments
s2 = Stock(name='AAPL', shares=50, price=125.3)
print(s2.name, s2.shares, s2.price)
```

Both approaches should work now! The `_init` function allows us to handle both positional and keyword arguments seamlessly. It also preserves the parameter names in the function signature, which makes the `help()` output more useful. The `help()` function in Python provides information about functions, classes, and modules, and having the parameter names intact makes this information more meaningful.

When you're done experimenting, you can exit the Python interpreter by running the following command:

```python
exit()
```
